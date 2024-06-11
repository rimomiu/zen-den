// This makes VSCode check types as if you are using TypeScript
//@ts-check
import { BrowserRouter, Routes, Route } from 'react-router-dom'

// import ErrorNotification from './components/ErrorNotification'
import HomePage from './components/Home'

import './App.css'

function App() {
    return (
        <BrowserRouter>
            <div className="container">
                <Routes>
                    <Route path="/" element={<HomePage />} />
                </Routes>
            </div>
        </BrowserRouter>
    )
}

export default App
