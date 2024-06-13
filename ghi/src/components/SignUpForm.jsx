// @ts-check
import { useState } from 'react'
import { Navigate } from 'react-router-dom'
import useAuthService from '../hooks/useAuthService'

export default function SignUpForm() {
    const [firstname, setFirstname] = useState('')
    const [lastname, setLastname] = useState('')
    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const { signup, user, error } = useAuthService()

    async function handleFormSubmit(e) {
        e.preventDefault()
        await signup({ firstname, lastname, email, username, password })
    }

    if (user) {
        return <Navigate to="/" />
    }

    return (
        <form onSubmit={handleFormSubmit}>
            {error && <div className="error">{error.message}</div>}
            <input
                type="text"
                value={firstname}
                onChange={(e) => setFirstname(e.target.value)}
                placeholder="Enter First Name"
            />
            <input
                type="text"
                value={lastname}
                onChange={(e) => setLastname(e.target.value)}
                placeholder="Enter Last Name"
            />

            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter Username"
            />

            <input
                type="text"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Enter Email"
            />
            <input
                type="password"
                name="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Enter Password"
            />
            <button type="submit">Sign Up</button>
        </form>
    )
}
