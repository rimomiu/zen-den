import { useState } from 'react'
import { TextField, Button, Box } from '@mui/material'

function AddCommentForm({ blogId, onCommentAdded }) {
    const [commentContent, setCommentContent] = useState('')

    const handleCommentSubmit = async () => {
        try {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/blogs/${blogId}/comments`,
                {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        body: commentContent,
                    }),
                }
            )
            if (!response.ok) {
                throw new Error('Failed to add comment')
            }
            const newComment = await response.json()
            // Pass the new comment to the parent component
            onCommentAdded(newComment)
            // Clear the comment content
            setCommentContent('')
        } catch (error) {
            console.error('Error adding comment:', error)
        }
    }

    return (
        <Box>
            <TextField
                label="Type your comment here"
                variant="outlined"
                value={commentContent}
                onChange={(e) => setCommentContent(e.target.value)}
                fullWidth
                multiline
                rows={4}
                margin="normal"
            />
            <Button
                variant="contained"
                color="primary"
                onClick={handleCommentSubmit}
            >
                Post Comment
            </Button>
        </Box>
    )
}

export default AddCommentForm
