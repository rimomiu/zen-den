import React from 'react'
import { Button, TextField, Box } from '@mui/material'

function CommentForm({ onSubmit, initialValues }) {
    const [values, setValues] = React.useState(
        initialValues || {
            content: '',
        }
    )

    const handleChange = (event) => {
        setValues({
            ...values,
            [event.target.name]: event.target.value,
        })
    }

    const handleSubmit = (event) => {
        event.preventDefault()
        onSubmit(values)
        setValues({
            content: '',
        })
    }

    return (
        <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
                margin="normal"
                required
                fullWidth
                id="content"
                label="Comment"
                name="content"
                value={values.content}
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
                Post Comment
            </Button>
        </Box>
    )
}

export default CommentForm
