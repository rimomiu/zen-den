from fastapi import APIRouter
from queries.blogs_queries import Blogs

router = APIRouter()

@router.post("/blogs")
def create_blogs(blog: Blogs):
    return blog
