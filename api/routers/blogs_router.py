from fastapi import APIRouter, Depends
from queries.blogs_queries import BlogRepository
from models.blogs import Blogs, CreateBlogs, Error
from typing import List, Union


router = APIRouter()


@router.post("/blogs")
def create_blogs(blog: CreateBlogs):
    return blog


@router.get("/blogs", response_model=Union[Error, List[Blogs]])
def get_blogs(
    repo: BlogRepository = Depends(),
):
    return repo.get_blogs()
