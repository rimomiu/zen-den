"""
User API Router
"""

from fastapi import APIRouter, Depends, HTTPException
from typing import Optional, List
from models.users import UserResponse, UserRequest, UserUpdate
from utils.authentication import hash_password
from queries.user_queries import UserQueries


router = APIRouter(tags=["Users"])


@router.get("/users/{username}", response_model=UserResponse)
async def get_user_by_username(
    username: str, user_queries: UserQueries = Depends()
) -> Optional[UserResponse]:
    """
    [GET] User by username
    """
    user = user_queries.get_by_username(username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.get("/users/id/{user_id}", response_model=UserResponse)
async def get_user_by_id(
    user_id: int, user_queries: UserQueries = Depends()
) -> Optional[UserResponse]:
    """
    [GET] User by user_id
    """
    user = user_queries.get_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users", response_model=UserResponse)
async def create_user(
    new_user: UserRequest, user_queries: UserQueries = Depends()
) -> UserResponse:
    """
    Create [POST] a user
        # Hash the password before passing it to the queries
    """
    hashed_password = hash_password(new_user.password)
    created_user = user_queries.create_user(new_user, hashed_password)
    return created_user


@router.delete("/users/{username}")
async def delete_user(
    username: str, user_queries: UserQueries = Depends()
) -> str:
    """
    [DELETE] User by username
    """
    deleted = user_queries.delete_user(username)
    if deleted != f"Deleted profile of {username}":
        raise HTTPException(status_code=404, detail="User not found")
    return deleted


@router.get("/users", response_model=List[UserResponse])
async def list_all_users(
    user_queries: UserQueries = Depends(),
) -> List[UserResponse]:
    """
    [GET] a list of all users in the database
    """
    users = user_queries.list_all_users()
    return users


@router.put("/users/{user_id}")
def update_user(
    user_id: int,
    user: UserUpdate,
    queries: UserQueries = Depends(),
) -> UserUpdate:
    """
    Update [PUT] username and email
    """
    updated_user = queries.update_user(
        user.username, user.email, user_id=user_id
    )
    return updated_user
