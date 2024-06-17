import { BrowserRouter, Routes, Route } from 'react-router-dom'
import AuthProvider from './components/AuthProvider' // Import AuthProvider
import Nav from './Nav'
import BlogList from './components/BlogList'
import HomePage from './components/Home'
import SignInForm from './components/SignInForm'
import SignUpForm from './components/SignUpForm'

function App() {
    return (
        <AuthProvider>
            <BrowserRouter>
                <Nav />
                <Routes>
                    <Route path="/blogs" element={<BlogList />} />
                    <Route path="/" element={<HomePage />} />
                    <Route path="/signin" element={<SignInForm />} />
                    <Route path="/signup" element={<SignUpForm />} />
                </Routes>
            </BrowserRouter>
        </AuthProvider>
    )
}

export default App
