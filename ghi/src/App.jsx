import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Nav from './Nav'
import BlogList from './components/BlogList'
import PostBlog from './components/PostBlog'
import HomePage from './components/Home'
import AuthProvider from './components/AuthProvider'

function App() {
    return (
        <BrowserRouter basename={import.meta.env.VITE_BASE}>
            <AuthProvider>
                <Nav />
                <Routes>
                    <Route path="/blogs" element={<BlogList />} />
                    <Route path="/" element={<HomePage />} />
                    <Route path="/blogs/new" element={<PostBlog />} />
                </Routes>
            </AuthProvider>
        </BrowserRouter>
    )
}

export default App
