import { useState, useEffect, useContext } from 'react'
import { Card, CardContent, TextField, Typography, Button } from '@mui/material'
import { useParams, useNavigate } from 'react-router-dom'
import { AuthContext } from './AuthProvider'

function PostCommentForm() {
    const { user } = useContext(AuthContext)
    const [comment, setComment] = useState('')
    const [error, setError] = useState(null)
    const { blogId } = useParams()
    const navigate = useNavigate()

    useEffect(() => {
        if (!user) {
            navigate('/signin')
        }
    }, [user, navigate])

    const handleCommentChange = (e) => {
        setComment(e.target.value)
    }

    const handlePostComment = async () => {
        if (!comment) {
            setError('Please enter a comment')
            return
        }

        const currentDate = new Date()
        const payload = {
            body: comment,
            blog_id: blogId,
            date_published: currentDate.toISOString().split('T')[0],
        }

        const commentUrl = `${
            import.meta.env.VITE_API_HOST
        }/blogs/${blogId}/comments`
        const response = await fetch(commentUrl, {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(payload),
        })

        if (response.ok) {
            setComment('')
            setError(null)
        } else {
            setError('Failed to post comment')
        }
    }

    return (
        <Card>
            <CardContent>
                <Typography variant="h6">Post a comment</Typography>
                <TextField
                    label="Comment"
                    value={comment}
                    onChange={handleCommentChange}
                    fullWidth
                    multiline
                    rows={4}
                />
                {error && (
                    <Typography variant="body2" color="error">
                        {error}
                    </Typography>
                )}
                <Button
                    onClick={handlePostComment}
                    variant="contained"
                    color="primary"
                >
                    Post Comment
                </Button>
            </CardContent>
        </Card>
    )
}

export default PostCommentForm
