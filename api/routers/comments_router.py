"""
Comments API Router
"""

from fastapi import APIRouter, Depends, HTTPException
from queries.comments_queries import CommentRepository
from models.comments import (
    Comments,
    CreateComment,
    Error,
    CommentResponse,
    CommentUpdate,
)
from typing import List, Union

router = APIRouter(tags=["Comments"])
repo = CommentRepository()


@router.post("/blogs/{blog_id}/comments", response_model=CommentResponse)
def create_comment(
    comment: CreateComment, repo: CommentRepository = Depends()
):
    """
    Create [POST] a comment
    """
    try:
        created_comment = repo.create_comment(comment)
        return created_comment
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error creating comment")


@router.put(
    "/blogs/{blog_id}/comments/{comment_id}",
    response_model=Union[CommentResponse, Error],
)
def update_comment(
    blog_id: int,
    comment_id: int,
    update: CommentUpdate,
    repo: CommentRepository = Depends(),
):
    """
    Update [PUT] comment by blog_id and comment_id
    """
    try:
        updated_comment = repo.update(comment_id, blog_id, update)
        if updated_comment is None:
            raise HTTPException(status_code=404, detail="Comment not found")
        return updated_comment
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error updating comment")


@router.delete("/blogs/{blog_id}/comments/{comment_id}")
def delete_comment(
    comment_id: int, repo: CommentRepository = Depends()
) -> bool:
    """
    Delete [DELETE] comment by comment_id
    """
    try:
        deleted = repo.delete(comment_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Comment not found")
        return True
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error deleting comment")


@router.get(
    "/comments/users/{author_id}", response_model=Union[List[Comments], Error]
)
def get_user_comments(
    author_id: int,
    repo: CommentRepository = Depends(),
) -> Union[List[Comments], Error]:
    """
    [GET] comments by author_id
    """
    try:
        comments = repo.get_comments_by_user(author_id)
        if not comments:
            raise HTTPException(status_code=404, detail="No comments here")
        return comments
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error retrieving")


@router.get(
    "/blogs/{blog_id}/comments", response_model=Union[Error, List[Comments]]
)
def get_blog_comments(
    blog_id: int,
    repo: CommentRepository = Depends(),
) -> Union[List[Comments], Error]:
    """
    [GET] comments by blog_id
    """
    try:
        comments = repo.get_comments_by_blog_id(blog_id)
        if not comments:
            raise HTTPException(status_code=404, detail="No comments of blog")
        return comments
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail="Error retrieving")
