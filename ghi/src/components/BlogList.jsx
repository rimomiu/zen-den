import { useState, useEffect } from 'react'
function BlogList() {
    const [blogs, setBlogs] = useState([])
    const getData = async () => {
        const response = await fetch(`${import.meta.env.VITE_API_HOST}/blogs/`)
        if (response.ok) {
            const data = await response.json()
            setBlogs(data)
            console.log(data)
        }
    }
    useEffect(() => {
        getData()
    }, [])
    return (
        <>
            <div>
                <h1>Blogs</h1>
            </div>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Blog Title</th>
                        <th>Author</th>
                        <th>Picture</th>
                        <th>Date</th>
                    </tr>
                </thead>
                <tbody>
                    {blogs.map((blog) => (
                        <tr key={blog.blog_id}>
                            <td>{blog.title}</td>
                            <td>{blog.author_id}</td>
                            <td>{blog.picture_url}</td>
                            <td>{blog.date_published}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </>
    )
}
export default BlogList
