import { useState } from 'react'
import { Button, TextField, Box } from '@mui/material'

function UpdateCommentForm({ comment, onUpdate }) {
    const [content, setContent] = useState(comment.body)

    const handleChange = (event) => {
        setContent(event.target.value)
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        onUpdate(comment.comment_id, content)
    }

    return (
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
                margin="normal"
                required
                fullWidth
                id="content"
                label="Update Comment"
                name="content"
                value={content}
                onChange={handleChange}
                autoComplete="content"
                autoFocus
            />
            <Button
                type="submit"
                fullWidth
                variant="contained"
                sx={{ mt: 3, mb: 2 }}
            >
                Update Comment
            </Button>
        </Box>
    )
}

export default UpdateCommentForm
