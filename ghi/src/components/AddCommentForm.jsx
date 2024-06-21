// import { useState, useContext } from 'react'
// import { TextField, Button, Box, Typography, Alert } from '@mui/material'
// import { AuthContext } from '.../AuthProvider'

// function AddCommentForm({ blogId, onCommentAdded }) {
//     const { user } = useContext(AuthContext)
//     const [commentContent, setCommentContent] = useState('')
//     const [error, setError] = useState('')
//     const [success, setSuccess] = useState('')

//     const handleCommentSubmit = async () => {
//         setError('')
//         setSuccess('')

//         if (!user) {
//             setError('You must be logged in to post a comment.')
//             return
//         }

//         try {
//             const response = await fetch(
//                 `${import.meta.env.VITE_API_HOST}/blogs/${blogId}/comments`,
//                 {
//                     method: 'POST',
//                     headers: {
//                         'Content-Type': 'application/json',
//                         Authorization: `Bearer ${user.token}`,
//                     },
//                     body: JSON.stringify({
//                         body: commentContent,
//                         blog_id: blogId,
//                     }),
//                 }
//             )

//             if (!response.ok) {
//                 throw new Error('Failed to add comment')
//             }

//             const newComment = await response.json()
//             onCommentAdded(newComment)
//             setCommentContent('')
//             setSuccess('Comment added successfully!')
//         } catch (error) {
//             setError(`Error adding comment: ${error.message}`)
//         }
//     }

//     return (
//         <Box>
//             {user ? (
//                 <>
//                     {error && <Alert severity="error">{error}</Alert>}
//                     {success && <Alert severity="success">{success}</Alert>}
//                     <TextField
//                         label="Type your comment here"
//                         variant="outlined"
//                         value={commentContent}
//                         onChange={(e) => setCommentContent(e.target.value)}
//                         fullWidth
//                         multiline
//                         rows={4}
//                         margin="normal"
//                     />
//                     <Button
//                         variant="contained"
//                         color="primary"
//                         onClick={handleCommentSubmit}
//                     >
//                         Post Comment
//                     </Button>
//                 </>
//             ) : (
//                 <Typography variant="body1">
//                     You must be logged in to post a comment.
//                 </Typography>
//             )}
//         </Box>
//     )
// }

// export default AddCommentForm
