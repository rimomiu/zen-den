from datetime import date
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class CommentResponse(BaseModel):
    comment_id: int
    body: str
    blog_id: int
    author_id: int
    date_published: date
