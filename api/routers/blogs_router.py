from fastapi import APIRouter, Depends
from queries.blogs_queries import BlogRepository
from models.blogs import Blogs, CreateBlogs, Error, BlogResponse
from typing import List, Union


router = APIRouter()
repo = BlogRepository()


@router.post("/blogs", response_model=BlogResponse)
def create_blogs(blogs: CreateBlogs):
    return repo.create_blogs(blogs)


@router.get("/blogs", response_model=Union[Error, List[Blogs]])
def get_blogs(
    repo: BlogRepository = Depends(),
):
    return repo.get_blogs()
