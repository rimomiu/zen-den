from fastapi import APIRouter
from queries.blogs_queries import Blogs

router = APIRouter()

@router.post("/blogs")
def create_blog(blog: Blogs):
    return blog
