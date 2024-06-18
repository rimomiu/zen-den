from fastapi import APIRouter, Depends
from queries.blogs_queries import BlogRepository
from models.blogs import (
    Blogs,
    CreateBlogs,
    Error,
    BlogResponse,
    BlogUpdate,
    BlogAuthorResponse,
)
from typing import List, Union
from models.users import UserResponse
from utils.authentication import try_get_jwt_user_data


router = APIRouter(tags=["Blogs"])
repo = BlogRepository()


@router.post("/blogs", response_model=BlogResponse)
def create_blogs(
    blogs: CreateBlogs, user: UserResponse = Depends(try_get_jwt_user_data)
):
    return repo.create_blogs(blogs)


@router.get("/blogs", response_model=Union[Error, List[BlogAuthorResponse]])
def get_blogs(
    repo: BlogRepository = Depends(),
):
    return repo.get_blogs()


@router.get(
    "/blogs/{blog_id}", response_model=Union[BlogAuthorResponse, Error]
)
def get_blog(
    blog_id: int,
    repo: BlogRepository = Depends(),
) -> Union[BlogAuthorResponse, Error]:
    return repo.get_blog_by_blog_id(blog_id)


@router.get(
    "/users/id/{author_id}/blogs", response_model=Union[Error, List[Blogs]]
)
def get_blog_by_author(
    author_id: int,
    repo: BlogRepository = Depends(),
) -> Union[BlogResponse, Error]:
    return repo.get_blog_by_user_id(author_id)


@router.put("/blogs/{blog_id}", response_model=Union[BlogResponse, Error])
def update_blog(
    blog_id: int,
    blog: BlogUpdate,
    repo: BlogRepository = Depends(),
) -> Union[BlogResponse, Error]:
    return repo.update(blog_id, blog)


@router.delete("/blogs/{blog_id}", response_model=bool)
def delete_blog(
    blog_id: int,
    repo: BlogRepository = Depends(),
) -> bool:
    return repo.delete(blog_id)
