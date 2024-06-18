import { useState, useEffect } from 'react'
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

function BlogDetail() {
    const [blog, setBlog] = useState({ user: {} })
    const [editMode, setEditMode] = useState(false)
    const [updatedBlog, setUpdatedBlog] = useState({})
    const { blogId } = useParams()
    const navigate = useNavigate()

    const fetchData = async () => {
        const blogsUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
        const response = await fetch(blogsUrl)
        console.log(response, 'test a response')

        if (response.ok) {
            const data = await response.json()
            setBlog(data)
            setUpdatedBlog(data)
            console.log(data, 'test data')
        }
    }

    const handleDelete = async () => {
        const deleteUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
        const response = await fetch(deleteUrl, { method: 'DELETE' })
        if (response.ok) {
            navigate('/blogs')
        }
    }

    const handleUpdate = async () => {
        const updateUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
        const response = await fetch(updateUrl, {
            method: 'PUT',
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
    })

    const handleChange = (e) => {
        setUpdatedBlog({
            ...updatedBlog,
            [e.target.name]: e.target.value,
        })
    }

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
                </CardContent>
            </Card>
        </Container>
    )
}

export default BlogDetail
