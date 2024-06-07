from datetime import datetime
from fastapi import FastAPI


from pydantic import BaseModel

# import os

app = FastAPI()


class CreateComment(BaseModel):
    body: str
    blog_id: int
    author_id: int
    date_published: datetime


class CommentResponse(BaseModel):
    body: str
    blog_id: int
    author_id: int
    date_published: datetime
    comment_id: int


class Comments(BaseModel):
    comment_id: int
    body: str
    blog_id: int
    author_id: int
    date_published: datetime


class Error(BaseModel):
    message: str


class CommentUpdate(BaseModel):
    body: str


class CommentUpdate(BaseModel):
    body: str
