import { useState, useEffect, useCallback, useContext } from 'react'
import { Card, CardContent, Typography, Button, Container } from '@mui/material'
import { useParams } from 'react-router-dom'
import { AuthContext } from '../components/AuthProvider'
import UpdateCommentForm from './UpdateCommentForm'

function CommentList() {
    const { user } = useContext(AuthContext)
    const [comments, setComments] = useState([])
    const [commentToUpdate, setCommentToUpdate] = useState(null)
    const { blogId } = useParams()

    const fetchComments = useCallback(async () => {
        const commentsUrl = `${
            import.meta.env.VITE_API_HOST
        }/blogs/${blogId}/comments`
        const response = await fetch(commentsUrl)

        if (response.ok) {
            const data = await response.json()
            setComments(data)
        }
    }, [blogId])

    useEffect(() => {
        fetchComments()
    }, [fetchComments])

    const handleUpdateClick = (comment) => {
        setCommentToUpdate(comment)
    }

    const handleCommentUpdate = async (commentId, updatedContent) => {
        const updateUrl = `${
            import.meta.env.VITE_API_HOST
        }/blogs/${blogId}/comments/${commentId}`
        const response = await fetch(updateUrl, {
            method: 'PUT',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ body: updatedContent }),
        })
        if (response.ok) {
            const updatedComment = await response.json()
            setComments((prevComments) =>
                prevComments.map((comment) =>
                    comment.comment_id === commentId ? updatedComment : comment
                )
            )
            setCommentToUpdate(null)
        } else {
            console.error('Failed to update comment')
        }
    }

    const handleDeleteClick = async (commentId) => {
        const deleteUrl = `${
            import.meta.env.VITE_API_HOST
        }/comments/${commentId}`
        const response = await fetch(deleteUrl, {
            method: 'DELETE',
            credentials: 'include',
        })
        if (response.ok) {
            setComments((prevComments) =>
                prevComments.filter(
                    (comment) => comment.comment_id !== commentId
                )
            )
        } else {
            console.error('Failed to delete comment')
        }
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
                        {user && user.user_id === comment.author_id && (
                            <>
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
                            </>
                        )}
                    </CardContent>
                </Card>
            ))}
            {commentToUpdate && (
                <UpdateCommentForm
                    comment={commentToUpdate}
                    onUpdate={handleCommentUpdate}
                />
            )}
        </Container>
    )
}

export default CommentList