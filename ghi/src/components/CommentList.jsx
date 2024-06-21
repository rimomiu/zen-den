import { useState, useEffect } from 'react'
import { Card, CardContent, Typography, Button, Container } from '@mui/material'
import { useParams } from 'react-router-dom'
import UpdateCommentForm from './UpdateCommentForm'
import AddCommentForm from './AddCommentForm'

function CommentList() {
    const [comments, setComments] = useState([])
    const [commentToUpdate, setCommentToUpdate] = useState(null)
    const { blogId } = useParams()

    useEffect(() => {
        const fetchComments = async () => {
            try {
                const commentsUrl = `${
                    import.meta.env.VITE_API_HOST
                }/blogs/${blogId}/comments`
                const response = await fetch(commentsUrl)
                if (!response.ok) {
                    throw new Error('Failed to fetch comments')
                }
                const data = await response.json()
                setComments(data)
            } catch (error) {
                console.error(error)
            }
        }

        fetchComments()
    }, [blogId])

    const handleUpdateClick = (comment) => {
        setCommentToUpdate(comment)
    }

    const handleCommentUpdate = async (commentId, updatedContent) => {
        try {
            const updateUrl = `${
                import.meta.env.VITE_API_HOST
            }/blogs/${blogId}/comments/${commentId}`
            const response = await fetch(updateUrl, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ body: updatedContent }),
            })
            if (!response.ok) {
                throw new Error('Failed to update comment')
            }
            const updatedComment = await response.json()
            setComments((prevComments) =>
                prevComments.map((comment) =>
                    comment.comment_id === commentId ? updatedComment : comment
                )
            )
            setCommentToUpdate(null)
        } catch (error) {
            console.error('Error updating comment:', error)
        }
    }

    const handleDeleteClick = async (commentId) => {
        try {
            const deleteUrl = `${
                import.meta.env.VITE_API_HOST
            }/blogs/${blogId}/comments/${commentId}`
            const response = await fetch(deleteUrl, { method: 'DELETE' })
            if (!response.ok) {
                throw new Error('Failed to delete comment')
            }
            setComments((prevComments) =>
                prevComments.filter(
                    (comment) => comment.comment_id !== commentId
                )
            )
        } catch (error) {
            console.error('Error deleting comment:', error)
        }
    }

    const handleCommentAdded = (newComment) => {
        setComments((prevComments) => [...prevComments, newComment])
    }

    return (
        <Container style={{ marginTop: '20px' }}>
            {comments.map((comment) => (
                <Card key={comment.comment_id} style={{ marginBottom: '20px' }}>
                    <CardContent>
                        <Typography variant="body1" gutterBottom>
                            {comment.body}
                        </Typography>
                        <Typography variant="body2" color="textSecondary">
                            By Author ID {comment.author_id} on{' '}
                            {comment.date_published}
                        </Typography>
                        <Button
                            onClick={() => handleUpdateClick(comment)}
                            variant="contained"
                            color="primary"
                            size="small"
                            style={{ marginRight: '10px' }}
                        >
                            Update
                        </Button>
                        <Button
                            onClick={() =>
                                handleDeleteClick(comment.comment_id)
                            }
                            variant="contained"
                            color="error"
                            size="small"
                        >
                            Delete
                        </Button>
                    </CardContent>
                </Card>
            ))}
            {/* Display the UpdateCommentForm component if there's a comment to update */}
            {commentToUpdate && (
                <UpdateCommentForm
                    comment={commentToUpdate}
                    onUpdate={handleCommentUpdate}
                />
            )}
            {/* Display the AddCommentForm component */}
            <AddCommentForm
                blogId={blogId}
                onCommentAdded={handleCommentAdded}
            />
        </Container>
    )
}

export default CommentList
