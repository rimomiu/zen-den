from datetime import datetime
from fastapi import FastAPI

# from fastapi.middleware.cors import CORSMiddleware
# from routers import auth_router
from pydantic import BaseModel

# import os

app = FastAPI()


class CreateBlogs(BaseModel):
    title: str
    author_id: int
    pic_url: str
    content: str
    date_published: datetime


class BlogResponse(BaseModel):
    title: str
    author_id: int
    pic_url: str
    content: str
    date_published: datetime
    blog_id: int


class Blogs(BaseModel):
    title: str
    pic_url: str
    content: str
    author_id: int


class Error(BaseModel):
    message: str
