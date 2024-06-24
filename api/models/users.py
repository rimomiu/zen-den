"""
Pydantic Models for Users
"""


from pydantic import BaseModel
from typing import Optional


class UserSignIn(BaseModel):
    username: str
    password: str


class UserRequest(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


class UserResponse(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: str
    user_id: int


class UserWithPw(UserRequest):
    user_id: int


class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]


class UserAsAuthor(BaseModel):
    user_id: int
    username: str
    first_name: str
    last_name: str


class Error(BaseModel):
    message: str
