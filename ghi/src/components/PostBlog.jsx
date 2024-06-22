import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Typography, Container, Button, IconButton, Box } from '@mui/material'
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
    const [message, setMessage] = useState('')
    const handleSubmit = async (e) => {
        e.preventDefault()
        console.log("I'M SUBMITTING WOOOOOOOOOOOOHOOOOOOOOOOO")
        try {
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
                setMessage('Successfully posted a blog!')
                setBlogPost({
                    title: '',
                    pic_url: '',
                    content: '',
                    date_published: '',
                    username: user.username,
                })
                navigate('/blogs')
            } else {
                setMessage('something went wrong, please try again')
            }
        } catch (e) {
            console.log(e)
        }
        // const handleNavigate = (event) => {
        //     event.preventDefault()
        //     navigate('/blogs')
    }

    return (
        <Container>
            <Box>
                <IconButton
                    aria-label="rnavigate back to events"
                    onClick={() => navigate('/events')}
                ></IconButton>

                <Typography variant="h2" component="h2" gutterBottom>
                    Post a blog
                </Typography>
                <form onSubmit={handleSubmit} id="create-blogpost">
                    <div className="form-floating mb-3">
                        <input
                            onChange={handleFormChange}
                            value={blogPost.title}
                            placeholder="title"
                            required
                            type="text"
                            name="title"
                            id="title"
                            className="form-control"
                        />
                        <label htmlFor="title">Title</label>
                    </div>
                    <div className="form-floating mb-3">
                        <input
                            onChange={handleFormChange}
                            value={blogPost.content}
                            placeholder="content"
                            required
                            type="text"
                            name="content"
                            id="content"
                            className="form-control"
                        />
                        <label htmlFor="content">Content</label>
                    </div>
                    <div className="form-floating mb-3">
                        <input
                            onChange={handleFormChange}
                            value={blogPost.pic_url}
                            placeholder="pic_url"
                            required
                            type="pic_url"
                            name="pic_url"
                            id="pic_url"
                            className="form-control"
                        />
                        <label htmlFor="Pic_url">Image URL</label>
                    </div>
                    <div className="form-floating mb-3">
                        <input
                            onChange={handleFormChange}
                            value={blogPost.date_published}
                            placeholder="date"
                            required
                            type="date"
                            name="date_published"
                            id="date"
                            className="form-control"
                        />
                        <label htmlFor="date">Date</label>
                    </div>
                    <div className="form-floating mb-3">
                        <input
                            onChange={handleFormChange}
                            value={blogPost.username}
                            placeholder="username"
                            required
                            type="text"
                            name="username"
                            id="username"
                            className="form-control"
                        />
                        <label htmlFor="username">username</label>
                    </div>
                    <Button className="btn btn-primary" type="submit">
                        Post
                    </Button>
                </form>
                {message && <p>{message}</p>}
            </Box>
        </Container>
    )
}
