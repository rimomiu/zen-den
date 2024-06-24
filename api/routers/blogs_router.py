"""
Blog API Router
"""

from fastapi import APIRouter, Depends, HTTPException, status
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
def create_blog(
    blogs: CreateBlogs,
    repo: BlogRepository = Depends(),
    user: UserResponse = Depends(try_get_jwt_user_data),
) -> BlogResponse:
    """
    [POST] Create a blog
    """
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please sign in to post a blog",
        )
    post_blog = repo.create_blogs(blogs, user.user_id)
    if not post_blog:
        raise HTTPException(status_code=400, detail="Unable to post blog")
    return post_blog


@router.get("/blogs", response_model=Union[Error, List[BlogAuthorResponse]])
def get_blogs(
    repo: BlogRepository = Depends(),
):
    """
    [GET] a list of all blogs
    """
    return repo.get_blogs()


@router.get(
    "/blogs/{blog_id}", response_model=Union[BlogAuthorResponse, Error]
)
def get_blog(
    blog_id: int,
    repo: BlogRepository = Depends(),
) -> Union[BlogAuthorResponse, Error]:
    """
    [GET] blog by blog_id
    """
    return repo.get_blog_by_blog_id(blog_id)


@router.get(
    "/users/id/{author_id}/blogs", response_model=Union[Error, List[Blogs]]
)
def get_blog_by_author(
    author_id: int,
    repo: BlogRepository = Depends(),
) -> Union[BlogResponse, Error]:
    """
    [GET] blog by author_id
    """
    return repo.get_blog_by_user_id(author_id)


@router.put("/blogs/{blog_id}", response_model=BlogResponse)
def update_blog(
    blog_id: int,
    blog: BlogUpdate,
    repo: BlogRepository = Depends(),
    user: UserResponse = Depends(try_get_jwt_user_data),
) -> BlogResponse:
    """
    [PUT] Update blog by blog_id
    """
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please sign in to update a blog",
        )
    return repo.update(blog_id, blog, user.user_id)


@router.delete("/blogs/{blog_id}", response_model=bool)
def delete_blog(
    blog_id: int,
    repo: BlogRepository = Depends(),
    user: UserResponse = Depends(try_get_jwt_user_data),
) -> bool:
    """
    [DELETE] blog by blog_id
    """
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sign in to delete blog.",
        )
    return repo.delete(blog_id, user.user_id)
