import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Nav from './Nav'
import BlogList from './components/BlogList'
// import PostBlog from './components/PostBlog'
import HomePage from './components/Home'

function App() {
    return (
        <BrowserRouter>
            <Nav />
            <Routes>
                <Route path="/blogs" element={<BlogList />} />
                <Route path="/" element={<HomePage />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App
