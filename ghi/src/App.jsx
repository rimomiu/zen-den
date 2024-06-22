import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Nav from './Nav'
import AuthProvider from './components/AuthProvider'
import BlogList from './components/BlogList'
import PostBlog from './components/PostBlog'
import HomePage from './components/Home'
import BlogDetail from './components/BlogDetail'
import Profile from './components/Profile'
import SignInForm from './components/SignInForm'
import SignUpForm from './components/SignUpForm'
// import ContactForm from './components/ContactForm'
import CommentList from './components/CommentList'

function App() {
    return (
        <BrowserRouter basename={import.meta.env.VITE_BASE}>
            <AuthProvider>
                <Nav />
                <Routes>
                    <Route path="/blogs" element={<BlogList />} />
                    <Route path="/blogs/:blogId" element={<BlogDetail />} />
                    <Route path="/blogs/new" element={<PostBlog />} />
                    <Route
                        path="/blogs/:blogId/comments"
                        element={<CommentList />}
                    />
                    <Route path="/" element={<HomePage />} />
                    <Route path="/user/id/:userId" element={<Profile />} />
                    <Route path="/signup" element={<SignUpForm />} />
                    <Route path="/signin" element={<SignInForm />} />
                </Routes>
            </AuthProvider>
        </BrowserRouter>
    )
}

export default App
