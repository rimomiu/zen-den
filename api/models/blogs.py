from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel
from models.users import UserAsAuthor

# import os

app = FastAPI()


class CreateBlogs(BaseModel):
    title: str
    author_id: int
    pic_url: str
    content: str
    date_published: date


class BlogResponse(BaseModel):
    title: str
    author_id: int
    pic_url: str
    content: str
    date_published: date
    blog_id: int


class Blogs(BaseModel):
    blog_id: int
    title: str
    pic_url: str
    content: str
    author_id: int
    date_published: date


class Error(BaseModel):
    message: str


class BlogUpdate(BaseModel):
    title: str
    pic_url: str
    content: str
