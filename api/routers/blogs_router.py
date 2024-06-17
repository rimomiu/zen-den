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
from typing import List, Union, Optional
from models.users import UserResponse
from utils.authentication import try_get_jwt_user_data


router = APIRouter()
repo = BlogRepository()


@router.post("/blogs", response_model=BlogResponse)
def create_blogs(
    blogs: CreateBlogs,
    repo: BlogRepository = Depends(),
    user: UserResponse = Depends(try_get_jwt_user_data),
):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please sign in to post a blog",
        )
    post_blog = repo.create(blogs)
    if not post_blog:
        raise HTTPException(status_code=500, detail="Unable to post blog")
    return post_blog


@router.get("/blogs", response_model=Union[Error, List[BlogAuthorResponse]])
def get_blogs(
    repo: BlogRepository = Depends(),
):
    return repo.get_blogs()


@router.get("/blogs/{blog_id}", response_model=Union[BlogResponse, Error])
def get_blog(
    blog_id: int,
    repo: BlogRepository = Depends(),
) -> Union[BlogResponse, Error]:
    return repo.get_blog_by_blog_id(blog_id)


@router.get(
    "/users/{author_id}/blogs", response_model=Union[Error, List[Blogs]]
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
    user: Optional[try_get_jwt_user_data] = Depends(try_get_jwt_user_data),
):
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sign in to delete blog.",
        )
    success = repo.delete(blog_id)
    if success:
        return success
    else:
        raise HTTPException(
            status_code=403, detail="Only authors can delete their blogs"
        )
