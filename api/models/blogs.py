from datetime import datetime
from fastapi import FastAPI


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
    blog_id: int
    title: str
    pic_url: str
    content: str
    author_id: int
    date_published: datetime


class Error(BaseModel):
    message: str


class BlogUpdate(BaseModel):
    title: str
    pic_url: str
    content: str
