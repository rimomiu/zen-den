//@ts-check
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'
import { createTheme, ThemeProvider } from '@mui/material/styles'

const BASE_URL = import.meta.env.BASE_URL
if (!BASE_URL) {
    throw new Error('BASE_URL is not defined')
}

const theme = createTheme({
    palette: {
        primary: {
            main: '#5A735B',
        },
        secondary: {
            main: '#B7BFAA',
        },
    },
    typography: {
        button: {
            fontSize: 20,
            color: '#B7BFA',
        },
        body1: {
            fontSize: '1rem',
            color: '#333', //
        },
    },
})

console.table(import.meta.env)

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
    <ThemeProvider theme={theme}>
        <React.StrictMode>
            <App />
        </React.StrictMode>
    </ThemeProvider>
)
