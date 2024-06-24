import { useState, useEffect } from 'react'
import {
    Container,
    Box,
    Typography,
    Card,
    CardMedia,
    CardContent,
} from '@mui/material'
import ContactForm from './ContactForm'

function HomePage() {
    const [blogs, setBlogs] = useState([])
    const [currentBlogIndex, setCurrentBlogIndex] = useState(0)

    useEffect(() => {
        const fetchBlogs = async () => {
            const response = await fetch(
                `${import.meta.env.VITE_API_HOST}/blogs/`
            )
            if (response.ok) {
                const data = await response.json()
                setBlogs(data)
            }
        }

        fetchBlogs()
    }, [])

    useEffect(() => {
        const intervalId = setInterval(() => {
            setCurrentBlogIndex((prevIndex) => (prevIndex + 1) % blogs.length)
        }, 10000) // Change every 10 seconds

        return () => clearInterval(intervalId) // Clean up the interval on component unmount
    }, [blogs.length])

    return (
        <>
            <Container>
                <Box my={4} textAlign="center">
                    {blogs?.length > 0 && (
                        <Card>
                            <CardMedia
                                component="img"
                                image={
                                    blogs[currentBlogIndex]?.pic_url ||
                                    'https://images.pexels.com/photos/6913382/pexels-photo-6913382.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2'
                                }
                                alt={blogs[currentBlogIndex]?.title}
                            />
                            <CardContent>
                                <Typography variant="h5" component="div">
                                    {blogs[currentBlogIndex]?.title}
                                </Typography>
                                <Typography
                                    variant="body2"
                                    color="textSecondary"
                                >
                                    {blogs[currentBlogIndex]?.user.username}
                                </Typography>
                                <Typography
                                    variant="body2"
                                    color="textSecondary"
                                >
                                    {blogs[currentBlogIndex]?.date_published}
                                </Typography>
                                <Typography variant="body1">
                                    {blogs[currentBlogIndex]?.content}
                                </Typography>
                            </CardContent>
                        </Card>
                    )}
                </Box>
                <Box>
                    <ContactForm />{' '}
                </Box>
            </Container>
        </>
    )
}

export default HomePage
