import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Nav from './Nav'
import AuthProvider from './components/AuthProvider' // Import AuthProvider

import BlogList from './components/BlogList'
import HomePage from './components/Home'
import BlogDetail from './components/BlogDetail'
import Profile from './components/Profile'
import SignInForm from './components/SignInForm'
import SignUpForm from './components/SignUpForm'
function App() {
    return (
        <AuthProvider>
            <BrowserRouter>
                <Nav />
                <Routes>
                    <Route path="/blogs" element={<BlogList />} />
                    <Route path="/blogs/:blogId" element={<BlogDetail />} />
                    <Route path="/" element={<HomePage />} />
                    <Route path="/user/:userId" element={<Profile />} />
                    <Route path="/signup" element={<SignUpForm />} />
                    <Route path="/signin" element={<SignInForm />} />
                </Routes>
            </BrowserRouter>
        </AuthProvider>
    )
}

export default App
