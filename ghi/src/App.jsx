import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Nav from './Nav'
import AuthProvider from './components/AuthProvider' // Import AuthProvider

import BlogList from './components/BlogList'
// import PostBlog from './components/PostBlog'
import HomePage from './components/Home'
import BlogDetail from './components/BlogDetail'
import Profile from './components/Profile'
import SignInForm from './components/SignInForm'
import SignUpForm from './components/SignUpForm'
import ContactForm from './components/ContactForm'
import CommentList from './components/CommentList'

function App() {
    return (
        <AuthProvider>
            <BrowserRouter>
                <Nav />
                <Routes>
                    <Route path="/blogs" element={<BlogList />} />
                    <Route path="/blogs/:blogId" element={<BlogDetail />} />
                    <Route
                        path="/blogs/:blogId/comments"
                        element={<CommentList />}
                    />
                    <Route path="/" element={<HomePage />} />
                    <Route path="/user/id/:userId" element={<Profile />} />
                    <Route path="/signup" element={<SignUpForm />} />
                    <Route path="/signin" element={<SignInForm />} />
                    <Route path="/contactme" element={<ContactForm />} />
                </Routes>
            </BrowserRouter>
        </AuthProvider>
    )
}

export default App
