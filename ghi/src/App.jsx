import { BrowserRouter, Routes, Route } from 'react-router-dom'
import BlogList from './components/BlogList'
import HomePage from './components/Home'

import './App.css'

function App() {
    return (
        <BrowserRouter>
            {' '}
            <h1>Vite + React</h1>
            <Routes>
                <Route path="/blogs" element={<BlogList />} />
                <Route path="/" element={<HomePage />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App
