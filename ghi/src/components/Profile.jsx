import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
// import 'profile.css'

function Profile() {
    const [users, setUsers] = useState([])
    const { userId } = useParams('')

    const fetchData = async () => {
        const usersUrl = `${import.meta.env.VITE_API_HOST}/users/${userId}`
        const response = await fetch(usersUrl)
        if (response.ok) {
            const data = await response.json()
            setUsers(data)
        }
    }

    useEffect(() => {
        fetchData()
    }, [])
    return (
        <>
            <div>
                <h1 className="title-pen"> User Profile </h1>
                <div className="user-profile">
                    <div className="username">{users.username}</div>
                    <div className="user_id">{users.user_id}</div>
                    <div className="description"></div>
                </div>
            </div>
        </>
    )
}
export default Profile
