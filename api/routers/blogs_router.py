"""
Blogs API Router
"""

from fastapi import APIRouter, Depends, HTTPException
from queries.blogs_queries import BlogRepository
from models.blogs import Blogs, CreateBlogs, Error, BlogResponse, BlogUpdate
from typing import List, Union
from models.users import UserResponse
from utils.authentication import try_get_jwt_user_data


router = APIRouter(tags=["Blogs"])
repo = BlogRepository()


@router.post("/blogs", response_model=BlogResponse)
def create_blogs(
    blogs: CreateBlogs, user: UserResponse = Depends(try_get_jwt_user_data)
):
    """
    Create [POST] blog
    """
    try:
        created_blog = repo.create_blogs(blogs)
        return created_blog
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error creating blog")


@router.get("/blogs", response_model=Union[Error, List[Blogs]])
def get_blogs(
    repo: BlogRepository = Depends(),
):
    """
    [GET] a list of all blogs
    """
    try:
        blogs = repo.get_blogs()
        if not blogs:
            raise HTTPException(status_code=404, detail="No blogs found")
        return blogs
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error retrieving blogs")


@router.get("/blogs/{blog_id}", response_model=Union[BlogResponse, Error])
def get_blog(
    blog_id: int,
    repo: BlogRepository = Depends(),
) -> Union[BlogResponse, Error]:
    """
    [GET] blog by blog_id
    """
    try:
        blog = repo.get_blog_by_id(blog_id)
        if blog is None:
            raise HTTPException(status_code=404, detail="Blog not found")
        return blog
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error retrieving blog")


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
    try:
        blogs = repo.get_blog_by_username(author_id)
        if not blogs:
            raise HTTPException(status_code=404, detail="No blog of author_id")
        return blogs
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error retrieving blogs")


@router.put("/blogs/{blog_id}", response_model=Union[BlogResponse, Error])
def update_blog(
    blog_id: int,
    blog: BlogUpdate,
    repo: BlogRepository = Depends(),
) -> Union[BlogResponse, Error]:
    """
    Update [PUT] blog by blog_id
    """
    try:
        updated_blog = repo.update(blog_id, blog)
        if updated_blog is None:
            raise HTTPException(status_code=404, detail="Error updating blog")
        return updated_blog
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error updating blog")


@router.delete("/blogs/{blog_id}", response_model=bool)
def delete_blog(
    blog_id: int,
    repo: BlogRepository = Depends(),
) -> bool:
    """
    [DELETE] blog by blog_id
    """
    try:
        deleted = repo.delete(blog_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Blog not found")
        return True
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error deleting blog")
