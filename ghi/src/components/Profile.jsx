import { useState, useEffect, useCallback } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import {
    Card,
    CardContent,
    Typography,
    Container,
    Grid,
    CircularProgress,
    CardActionArea,
    Button,
} from '@mui/material'

import { signout } from '../services/authService'

export default function Profile() {
    const [user, setUser] = useState([])
    const [blogs, setBlogs] = useState([])
    const [comments, setComments] = useState([])
    const { userId } = useParams()
    const navigate = useNavigate()

    const fetchData = useCallback(async () => {
        const userUrl = `${import.meta.env.VITE_API_HOST}/users/id/${userId}`
        const blogsUrl = `${
            import.meta.env.VITE_API_HOST
        }/users/${userId}/blogs`
        const commentUrl = `${
            import.meta.env.VITE_API_HOST
        }/comments/users/${userId}`

        const userResponse = await fetch(userUrl)
        const blogsResponse = await fetch(blogsUrl)
        const commentResponse = await fetch(commentUrl)

        if (userResponse.ok && blogsResponse.ok) {
            const userData = await userResponse.json()
            const blogsData = await blogsResponse.json()

            setUser(userData)
            setBlogs(blogsData)
        }
        if (commentResponse.ok) {
            const commentsData = await commentResponse.json()
            setComments(commentsData)
        }
    }, [userId])

    useEffect(() => {
        fetchData()
    }, [fetchData])

    const handleDeleteBlog = async (blogId) => {
        const deleteUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
        const response = await fetch(deleteUrl, {
            method: 'DELETE',
            credentials: 'include',
        })
        if (response.ok) {
            fetchData()
        }
    }

    const handleDeleteComment = async (commentId) => {
        const deleteUrl = `${
            import.meta.env.VITE_API_HOST
        }/comments/${commentId}`
        const response = await fetch(deleteUrl, {
            method: 'DELETE',
            credentials: 'include',
        })
        if (response.ok) {
            fetchData()
        }
    }

    const handleLogout = () => {
        signout()
        navigate('/')
        window.location.reload()
    }

    if (!user) {
        return <CircularProgress />
    }

    return (
        <Container>
            <Typography variant="h2" component="h2" gutterBottom>
                User Profile
            </Typography>
            <Button variant="contained" color="primary" onClick={handleLogout}>
                Logout
            </Button>
            <Card>
                <CardContent>
                    <Typography variant="h6" component="p">
                        Username: {user.username}
                    </Typography>
                    <Typography variant="h6" component="p">
                        First Name: {user.first_name}
                    </Typography>
                    <Typography variant="h6" component="p">
                        Last Name: {user.last_name}
                    </Typography>
                </CardContent>
            </Card>

            <Typography variant="h4" component="h4" gutterBottom>
                User Blog
            </Typography>
            <Grid container spacing={2}>
                {blogs.map((blog) => {
                    return (
                        <Grid item xs={12} sm={6} md={4} key={blog.blog_id}>
                            <Card>
                                <CardActionArea
                                    component={Link}
                                    to={`/blogs/${blog.blog_id}`}
                                >
                                    <CardContent>
                                        <Typography variant="h5" component="h4">
                                            {blog.title}
                                        </Typography>
                                        <Typography
                                            variant="body2"
                                            component="p"
                                        >
                                            {blog.date_publish}
                                        </Typography>
                                    </CardContent>
                                </CardActionArea>
                                <CardContent>
                                    <Button
                                        variant="contained"
                                        color="error"
                                        onClick={() =>
                                            handleDeleteBlog(blog.blog_id)
                                        }
                                        size="small"
                                    >
                                        Delete Blog
                                    </Button>
                                </CardContent>
                            </Card>
                        </Grid>
                    )
                })}
            </Grid>
            <Typography variant="h4" component="h4" gutterBottom>
                User Comments
            </Typography>
            <Grid container spacing={2}>
                {comments.map((comment) => (
                    <Grid item xs={12} sm={6} md={4} key={comment.comment_id}>
                        <Card>
                            <CardContent>
                                <Typography variant="h5" component="h4">
                                    {comment.body}
                                </Typography>
                            </CardContent>
                            <CardContent>
                                <Button
                                    variant="contained"
                                    color="error"
                                    onClick={() =>
                                        handleDeleteComment(comment.comment_id)
                                    }
                                    size="small"
                                >
                                    Delete Comment
                                </Button>
                            </CardContent>
                        </Card>
                    </Grid>
                ))}
            </Grid>
        </Container>
    )
}
