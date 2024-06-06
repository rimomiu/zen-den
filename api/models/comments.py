from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()


class Error(BaseModel):
    message: str


class Comments(BaseModel):
    comment_id: int
    body: str
    blog_id: int
    author_id: int
    date_published: date
