//@ts-check
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'

const BASE_URL = import.meta.env.BASE_URL
if (!BASE_URL) {
    throw new Error('BASE_URL is not defined')
}

// const router = createBrowserRouter(
//     [
//         {
//             path: '/',
//             element: <App />,
//             children: [
//                 {
//                     path: '',
//                     element: <HomePage />,
//                 },
//                 {
//                     path: 'signup',
//                     element: <SignUpForm />,
//                 },
//                 {
//                     path: 'signin',
//                     element: <SignInForm />,
//                 },
//             ],
//         },
//     ],
//     {
//         basename: BASE_URL,
//     }
// )

// const rootElement = document.getElementById('root')
// if (!rootElement) {
//     throw new Error('root element was not found!')
// }

// Log out the environment variables while you are developing and deploying
// This will help debug things
console.table(import.meta.env)

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
    <React.StrictMode>
        <App />
    </React.StrictMode>
)
