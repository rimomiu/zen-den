import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Typography, Container, Button, TextField, Box } from '@mui/material'
import useAuthService from './../hooks/useAuthService'

export default function PostBlog() {
    const { user } = useAuthService()
    const navigate = useNavigate()
    const [blogPost, setBlogPost] = useState({
        title: '',
        pic_url: '',
        content: '',
        date_published: '',
        username: user.username,
    })
    const handleFormChange = (e) => {
        const value = e.target.value
        const inputName = e.target.name
        setBlogPost({
            ...blogPost,
            [inputName]: value,
        })
    }
    const handleSubmit = async (e) => {
        e.preventDefault()
        const url = `${import.meta.env.VITE_API_HOST}/blogs/`
        const fetchConfig = {
            method: 'post',
            credentials: 'include',
            body: JSON.stringify(blogPost),
            headers: {
                'Content-Type': 'application/json',
            },
        }
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            setBlogPost({
                title: '',
                pic_url: '',
                content: '',
                date_published: '',
                username: user.username,
            })
            navigate('/blogs')
        }
    }

    return (
        <Container>
            <Box>
                <Typography variant="h1" color="#425130">
                    Post a blog
                </Typography>
                <Box
                    height={800}
                    width={1100}
                    my={5}
                    align="center"
                    gap={20}
                    p={10}
                    sx={{ border: '3px solid green' }}
                >
                    <form onSubmit={handleSubmit} id="create-blogpost">
                        <Box width={900}>
                            <TextField
                                onChange={handleFormChange}
                                value={blogPost.title}
                                placeholder="title"
                                required
                                type="text"
                                name="title"
                                id="title"
                                sx={{
                                    width: 800,
                                    '& .MuiInputBase-root': { height: 40 },
                                }}
                            />
                        </Box>
                        <Box>
                            <TextField
                                onChange={handleFormChange}
                                value={blogPost.content}
                                placeholder="Content"
                                required
                                type="text"
                                name="content"
                                id="content"
                                sx={{
                                    width: 800,
                                    '& .MuiInputBase-root': { height: 350 },
                                }}
                            />
                        </Box>
                        <Box>
                            <TextField
                                onChange={handleFormChange}
                                value={blogPost.pic_url}
                                placeholder="Image URL"
                                required
                                type="pic_url"
                                name="pic_url"
                                id="pic_url"
                                sx={{
                                    width: 800,
                                    '& .MuiInputBase-root': { height: 40 },
                                }}
                            />
                        </Box>
                        <Box>
                            <TextField
                                onChange={handleFormChange}
                                value={blogPost.date_published}
                                placeholder="date"
                                required
                                type="date"
                                name="date_published"
                                id="date"
                            />
                            <Typography>Published on</Typography>
                        </Box>
                        <Box>
                            <TextField
                                onChange={handleFormChange}
                                value={blogPost.username}
                                placeholder="By"
                                required
                                type="text"
                                name="username"
                                id="username"
                            />
                            <Typography>Authored By</Typography>
                        </Box>
                        <Button variant="contained" type="submit">
                            Post
                        </Button>
                    </form>
                </Box>
            </Box>
        </Container>
    )
}
