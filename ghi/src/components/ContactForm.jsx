import { useRef, useState } from 'react'
import emailjs from '@emailjs/browser'
import {
    Card,
    CardContent,
    Typography,
    Container,
    Button,
    TextField,
    Box,
    Alert,
} from '@mui/material'

const ContactForm = () => {
    const form = useRef()
    const [successMessage, setSuccessMessage] = useState('')

    const sendEmail = (e) => {
        e.preventDefault()

        emailjs
            .sendForm('service_wrw35zn', 'template_bl4xc8i', form.current, {
                publicKey: 'mZuKDUgplY0RgRMoX',
            })
            .then(
                () => {
                    setSuccessMessage(
                        'Your message has been sent successfully!'
                    )
                },
                (error) => {
                    console.log('FAILED...', error.text)
                }
            )
    }

    return (
        <Container style={{ marginTop: '100px' }}>
            <Card>
                <CardContent>
                    <Typography variant="h5" component="div" gutterBottom>
                        Contact Us
                    </Typography>
                    {successMessage && (
                        <Alert
                            severity="success"
                            style={{ marginBottom: '20px' }}
                        >
                            {successMessage}
                        </Alert>
                    )}
                    <form ref={form} onSubmit={sendEmail}>
                        <Box mb={2}>
                            <TextField
                                fullWidth
                                label="Name"
                                name="user_name"
                                variant="outlined"
                            />
                        </Box>
                        <Box mb={2}>
                            <TextField
                                fullWidth
                                label="Email"
                                name="user_email"
                                type="email"
                                variant="outlined"
                            />
                        </Box>
                        <Box mb={2}>
                            <TextField
                                fullWidth
                                label="Message"
                                name="message"
                                multiline
                                rows={4}
                                variant="outlined"
                            />
                        </Box>
                        <Button
                            variant="contained"
                            color="primary"
                            type="submit"
                        >
                            Send
                        </Button>
                    </form>
                </CardContent>
            </Card>
        </Container>
    )
}

export default ContactForm
