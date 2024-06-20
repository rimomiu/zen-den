import { useState } from 'react'
// import { useNavigate } from 'react-couter-dom'
// import { useAuthService } from '../hooks/useAuthService'
import { AuthContext } from './AuthProvider'

// import {
//     Card,
//     Box,
//     CardContent,
//     CardMedia,
//     CardActionArea,
//     Container,
//     Typography,
//     Grid,
//     TextField,
// } from '@mui/material'
function PostBlog() {
    const [authState, setAuthState] = AuthContext
    const [message, setMessage] = useState('')
    const [formData, setFormData] = useState({
        title: '',
        pic_url: '',
        content: '',
        date_published: '',
    })

    const handlePostForm = async (e) => {
        const data = e.target.value
        const inputName = e.target.name
        setFormData({
            ...formData,
            [inputName]: data,
        })
    }
    const handleSubmit = async (e) => {
        e.preventDefault()
        const url = `${import.meta.env.VITE_API_HOST}/blogs/`
        const fetchConfig = {
            method: 'post',
            body: JSON.stringify(formData),
            headers: {
                'Content-Type': 'application/json',
            },
            credentials: 'include',
        }
        const response = await fetch(url, fetchConfig)
        if (response.ok) {
            setMessage('Successfully added blog!')
            setFormData({
                title: '',
                pic_url: '',
                content: '',
                date_published: '',
            })
        } else {
            setMessage('Something went wrong, please try again')
            if (response.status === 401) {
                setAuthState({ authenticated: false, ...authState })
            }
        }
    }
    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Post a blog!</h1>
                    <form onSubmit={handleSubmit} id="create-appointment-form">
                        <div className="form-floating mb-3">
                            <input
                                onChange={handlePostForm}
                                value={formData.title}
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
                                onChange={handlePostForm}
                                value={formData.pic_url}
                                placeholder="pic_url"
                                required
                                type="text"
                                name="pic_url"
                                id="pic_url"
                                className="form-control"
                            />
                            <label htmlFor="pic_url">Image URL</label>
                        </div>
                        <div className="form-floating mb-3">
                            <input
                                onChange={handlePostForm}
                                value={formData.content}
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
                            <select
                                onChange={handlePostForm}
                                value={formData.date_published}
                                required
                                type="datetime-local"
                                name="date"
                                id="date"
                                className="form-control"
                            ></select>
                        </div>
                        <button className="btn btn-primary">Create</button>
                    </form>
                    {message && <p>{message}</p>}
                </div>
            </div>
        </div>
    )
}

export default PostBlog
