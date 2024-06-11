"""
Unit Tests for User endpoints
"""

from main import app
from fastapi.testclient import TestClient
from queries.user_queries import UserQueries
from models.users import UserResponse, UserRequest
from typing import List, Optional


client = TestClient(app)


"""
Unit-Test Base Case
"""


def test_init():
    assert 1 == 1


"""
Unit-Test [GET] user by username
"""


class TestGetUserByUsernameQueries:
    def get_by_username(self, username: str) -> Optional[UserResponse]:
        if username == "testuser":
            return UserResponse(
                username="testuser",
                first_name="Test",
                last_name="User",
                email="testuser@example.com",
                user_id=1,
                admin=False,
            )
        return None


def test_get_user_by_username():
    app.dependency_overrides[UserQueries] = TestGetUserByUsernameQueries

    response = client.get("/api/users/testuser")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {
        "username": "testuser",
        "first_name": "Test",
        "last_name": "User",
        "email": "testuser@example.com",
        "user_id": 1,
        "admin": False,
    }


"""
Unit-Test [POST] create user
"""


class TestCreateUserQueries:
    def create_user(
        self, new_user: UserRequest, hashed_password: str
    ) -> UserResponse:
        return UserResponse(
            username=new_user.username,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            email=new_user.email,
            user_id=1,
            admin=False,
        )


def test_create_user():
    app.dependency_overrides[UserQueries] = TestCreateUserQueries

    json_data = {
        "username": "newuser",
        "password": "password123",
        "first_name": "New",
        "last_name": "User",
        "email": "newuser@example.com",
    }
    expected = {
        "username": "newuser",
        "first_name": "New",
        "last_name": "User",
        "email": "newuser@example.com",
        "user_id": 1,
        "admin": False,
    }

    response = client.post("/api/users/", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


"""
Unit-Test [DELETE] user by username
"""


class TestDeleteUserQueries:
    def delete(self, username: str) -> str:
        if username == "testuser":
            return "Deleted profile of testuser"
        return "Could not delete"


def test_delete_user():
    app.dependency_overrides[UserQueries] = TestDeleteUserQueries

    response = client.delete("/api/users/testuser")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == "Deleted profile of testuser"


"""
Unit-Test [GET] all users
"""


class TestListAllUsersQueries:
    def list_all_users(self) -> List[UserResponse]:
        return [
            UserResponse(
                username="testuser",
                first_name="Test",
                last_name="User",
                email="testuser@example.com",
                user_id=1,
                admin=False,
            )
        ]


def test_list_all_users():
    app.dependency_overrides[UserQueries] = TestListAllUsersQueries

    response = client.get("/api/users/")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == [
        {
            "username": "testuser",
            "first_name": "Test",
            "last_name": "User",
            "email": "testuser@example.com",
            "user_id": 1,
            "admin": False,
        }
    ]
