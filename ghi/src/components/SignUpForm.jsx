// @ts-check
import { useState } from 'react'
import { Navigate } from 'react-router-dom'
import useAuthService from '../hooks/useAuthService'

export default function SignUpForm() {
    const [username, setUsername] = useState('')
    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')
    const [first_name, setFirstname] = useState('')
    const [last_name, setLastname] = useState('')
    const { signup, user, error } = useAuthService()

    async function handleFormSubmit(e) {
        e.preventDefault()
        await signup({
            username,
            password,
            first_name,
            last_name,
            email,
        })
    }

    if (user) {
        return <Navigate to="/" />
    }

    return (
        <>
            Sign Up
            <form onSubmit={handleFormSubmit}>
                {error && <div className="error">{error.message}</div>}
                <input
                    type="text"
                    name="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Enter Username"
                    required
                />
                <input
                    type="password"
                    name="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Enter Password"
                    required
                />
                <input
                    type="text"
                    name="firstname"
                    value={first_name}
                    onChange={(e) => setFirstname(e.target.value)}
                    placeholder="Enter First name"
                    required
                />
                <input
                    type="text"
                    name="lastname"
                    value={last_name}
                    onChange={(e) => setLastname(e.target.value)}
                    placeholder="Last Name"
                    required
                />
                <input
                    type="email"
                    name="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Enter Email"
                    required
                />
                <button
                    type="submit"
                    disabled={!username || !password || !email}
                >
                    Sign Up
                </button>
            </form>
        </>
    )
}
