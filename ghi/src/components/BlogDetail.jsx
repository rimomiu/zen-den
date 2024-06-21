import { useState, useEffect, useCallback, useContext } from 'react'
import {
    Card,
    CardContent,
    CardMedia,
    Container,
    Typography,
    TextField,
    Button,
} from '@mui/material'
import { useParams, useNavigate } from 'react-router-dom'
import { AuthContext } from './AuthProvider'
import CommentForm from './CommentForm'

function BlogDetail() {
    const { user } = useContext(AuthContext)
    const [blog, setBlog] = useState({ user: {} })
    const [editMode, setEditMode] = useState(false)
    const [updatedBlog, setUpdatedBlog] = useState({})
    const { blogId } = useParams()
    const navigate = useNavigate()

    const fetchData = useCallback(async () => {
        const blogsUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
        const response = await fetch(blogsUrl)

        if (response.ok) {
            const data = await response.json()
            setBlog(data)
            setUpdatedBlog(data)
        }
    }, [blogId])

    const handleDelete = async () => {
        const deleteUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
        const response = await fetch(deleteUrl, {
            method: 'DELETE',
            credentials: 'include',
        })
        if (response.ok) {
            navigate('/blogs')
        }
    }

    const handleUpdate = async () => {
        const updateUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
        const response = await fetch(updateUrl, {
            method: 'PUT',
            credentials: 'include',

            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(updatedBlog),
        })
        if (response.ok) {
            setEditMode(false)
            fetchData()
        }
    }

    useEffect(() => {
        fetchData()
    }, [fetchData])

    const handleChange = (e) => {
        setUpdatedBlog({
            ...updatedBlog,
            [e.target.name]: e.target.value,
        })
    }

    const isAuthor = user && user.id === blog.user.id

    return (
        <Container style={{ marginTop: '100px' }}>
            <Card>
                <CardContent>
                    {editMode ? (
                        <div>
                            <TextField
                                label="Title"
                                name="title"
                                value={updatedBlog.title}
                                onChange={handleChange}
                                fullWidth
                            />
                            <TextField
                                label="Pic_url"
                                name="pic_url"
                                value={updatedBlog.pic_url}
                                onChange={handleChange}
                                fullWidth
                            />
                            <TextField
                                label="Content"
                                name="content"
                                value={updatedBlog.content}
                                onChange={handleChange}
                                multiline
                                rows={10}
                                fullWidth
                            />

                            <Button
                                onClick={handleUpdate}
                                variant="contained"
                                color="primary"
                            >
                                Update
                            </Button>
                        </div>
                    ) : (
                        <div>
                            <Typography variant="h4">{blog.title}</Typography>
                            <Typography variant="h6">
                                Author: {blog.user.username}
                            </Typography>
                            <Typography variant="h6">
                                Published on: {blog.date_published}
                            </Typography>
                            <CardMedia
                                component="img"
                                image={blog.pic_url}
                                alt={blog.title}
                            />
                            <Typography variant="body1">
                                {blog.content}
                            </Typography>
                        </div>
                    )}
                    {isAuthor && (
                        <>
                            <Button
                                onClick={() => setEditMode(!editMode)}
                                variant="contained"
                                color="secondary"
                                size="small"
                            >
                                {editMode ? 'Cancel' : 'Edit'}
                            </Button>
                            <Button
                                onClick={handleDelete}
                                variant="contained"
                                color="error"
                                size="small"
                            >
                                Delete
                            </Button>
                        </>
                    )}
                </CardContent>
            </Card>
            <Card>
                <CommentForm />
            </Card>
        </Container>
    )
}

export default BlogDetail
