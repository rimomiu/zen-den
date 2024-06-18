// import { useState, useEffect } from 'react'
// import { useParams } from 'react-router-dom'
// import {
//     Card,
//     CardContent,
//     Typography,
//     Container,
//     Grid,
//     CircularProgress,
// } from '@mui/material'

// export default function Profile() {
//     const [user, setUser] = useState([])
//     const [blogs, setBlogs] = useState([])
//     const [comments, setComments] = useState([])
//     const { userId } = useParams()
//     const { blogId } = useParams()
//     const { commentId } = useParams()

//     const fetchData = async () => {
//         const userUrl = `${import.meta.env.VITE_API_HOST}/users/id/${userId}`
//         const blogsUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
//         const commentUrl = `${
//             import.meta.env.VITE_API_HOST
//         }/comments/${commentId}`

//         const userResponse = await fetch(userUrl)
//         const blogsResponse = await fetch(blogsUrl)
//         const commentResponse = await fetch(commentUrl)

//         if (userResponse.ok && blogsResponse.ok && commentResponse.ok) {
//             const userData = await userResponse.json()
//             const blogsData = await blogsResponse.json()
//             const commentData = await commentResponse.json()

//             setUser(userData)
//             setBlogs(blogsData)
//             setComments(commentsData)
//         }
//     }

//     useEffect(() => {
//         fetchData()
//     })

//     if (!user) {
//         return <CircularProgress />
//     }

//     return (
//         <Container>
//             <Typography variant="h2" component="h2" gutterBottom>
//                 User Profile
//             </Typography>
//             <Card>
//                 <CardContent>
//                     <Typography variant="h6" component="p">
//                         Username: {user.username}
//                     </Typography>
//                     <Typography variant="h6" component="p">
//                         First Name: {user.firstName}
//                     </Typography>
//                     <Typography variant="h6" component="p">
//                         Last Name: {user.lastName}
//                     </Typography>
//                 </CardContent>
//             </Card>

//             <Typography variant="h4" component="h4" gutterBottom>
//                 Users' Blog
//             </Typography>
//             <Grid container spacing={2}>
//                 {blogs.map((blog) => (
//                     <Grid item xs={12} sm={6} md={4} key={blog.id}>
//                         <Card>
//                             <CardContent>
//                                 <Typography variant="h5" component="h4">
//                                     {blog.title}
//                                 </Typography>
//                                 <Typography variant="body2" component="p">
//                                     {blog.date_publish}
//                                 </Typography>
//                             </CardContent>
//                         </Card>
//                     </Grid>
//                 ))}
//             </Grid>
//             <Typography variant="h4" component="h4" gutterBottom>
//                 Users' Comments
//             </Typography>
//             <Grid container spacing={2}>
//                 {comments.map((comment) => (
//                     <Grid item xs={12} sm={6} md={4} key={comment.id}>
//                         <Card>
//                             <CardContent>
//                                 <Typography variant="h5" component="h4">
//                                     {comment.body}
//                                 </Typography>
//                             </CardContent>
//                         </Card>
//                     </Grid>
//                 ))}
//             </Grid>
//         </Container>
//     )
// }
