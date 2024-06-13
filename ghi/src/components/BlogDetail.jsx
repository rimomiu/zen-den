//
import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
const BlogDetail = () => {
    const [blogs, setBlogs] = useState([])
    // const [comments,setComments]=useState([])
    const { blogId } = useParams('')
    // const { commentId } = useParams('')

    const fetchData = async () => {
        const blogsUrl = `${import.meta.env.VITE_API_HOST}/blogs/${blogId}`
        const response = await fetch(blogsUrl)
        if (response.ok) {
            const data = await response.json()
            setBlogs(data)
        }
    }

    useEffect(() => {
        fetchData()
    }, [])

    return (
        <div>
            <div>
                <h1>{blogs.title}</h1>
            </div>

            <div>
                <h2>Author:{blogs.author_id}</h2>
                <h3>Published on: {blogs.date_published}</h3>
            </div>
            <img src={blogs.pic_url} alt={blogs.title} />
            <p>{blogs.content}</p>
        </div>
    )
}

export default BlogDetail
