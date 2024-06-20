import { useState, useEffect } from 'react'
import {
    Card,
    Box,
    CardContent,
    CardMedia,
    CardActionArea,
    Container,
    Typography,
    Grid,
    TextField,
} from '@mui/material'
import { Link } from 'react-router-dom'

function BlogList() {
    const [blogs, setBlogs] = useState([])
    const [search, setSearch] = useState('') // Empty string for search

    const getData = async () => {
        const response = await fetch(`${import.meta.env.VITE_API_HOST}/blogs/`)
        if (response.ok) {
            const data = await response.json()
            setBlogs(data)
        }
    }

    useEffect(() => {
        getData()
    }, [])

    return (
        <>
            <Container fixed>
                <Box topmargin={80} margin={180} height={5} width={800} my={10}>
                    <TextField
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                        placeholder="Search by Keyword"
                        required
                    />
                </Box>
            </Container>
            <Grid container spacing={5}>
                {blogs
                    .filter((blog) =>
                        search
                            ? blog.title
                                  .toLowerCase()
                                  .includes(search.toLowerCase())
                            : true
                    )
                    .map((blog) => (
                        <Grid item key={blog.blog_id} md={4}>
                            {/* Use CSS classes for styling */}
                            <Card className="cardHover">
                                <CardActionArea
                                    component={Link}
                                    to={`/blogs/${blog.blog_id}`}
                                >
                                    <CardMedia
                                        component="img"
                                        className="cardImage"
                                        image={
                                            blog.pic_url ||
                                            'https://images.pexels.com/photos/6913382/pexels-photo-6913382.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
                                        }
                                        alt={blog.title}
                                    />
                                    <CardContent
                                        align="center"
                                        sx={{ backgroundColor: '#B7BFAA' }}
                                    >
                                        <Typography
                                            variant="h6"
                                            color="#5A735B"
                                        >
                                            {blog.title}
                                        </Typography>
                                        <Typography
                                            variant="h6"
                                            color="#5A735B"
                                        >
                                            <b>Author:</b> {blog.user.username}
                                        </Typography>
                                        <Typography
                                            variant="h7"
                                            color="#5A735B"
                                        >
                                            {blog.date_published}
                                        </Typography>
                                    </CardContent>
                                </CardActionArea>
                            </Card>
                        </Grid>
                    ))}
            </Grid>
        </>
    )
}

export default BlogList
