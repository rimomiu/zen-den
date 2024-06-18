// import { useState, useEffect } from 'react'
// import { useParams } from 'react-router-dom'

// export default function Profile() {
//     const [users, setUsers] = useState('')
//     const [blogs, setBlogs] = useState([])
//     const { userId } = useParams('')

//     const fetchData = async () => {
//         const userUrl = `${import.meta.env.VITE_API_HOST}/users/${userId}`
//         const response = await fetch(userUrl)
//         if (response.ok) {
//             const data = await response.json()
//             setUsers(data.users)
//             setBlogs(data.blogs)
//         }
//     }

//     useEffect(() => {
//         fetchData()
//     }, [userId])

//     if (!users) {
//         return <div>Loading...</div>
//     }

//     return (
//         <div>
//             <h2>User Profile</h2>
//             <p>Username: {users.username}</p>
//             <p>First Name: {users.firstName}</p>
//             <p>Last Name: {users.lastName}</p>
//             <h3>User Blogs</h3>
//             <ul>
//                 {blogs.map((blog) => (
//                     <li key={blog.id}>
//                         <h4>{blog.title}</h4>
//                         <p>{blog.content}</p>
//                     </li>
//                 ))}
//             </ul>
//         </div>
//     )
// }
