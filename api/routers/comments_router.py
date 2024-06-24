"""
Comment API Router
"""

from fastapi import APIRouter, Depends, HTTPException, status
from queries.comments_queries import CommentRepository
from models.comments import (
    Comments,
    CreateComment,
    Error,
    CommentResponse,
    CommentUpdate,
)
from models.users import UserResponse
from typing import List, Union
from utils.authentication import try_get_jwt_user_data

router = APIRouter(tags=["Comments"])
repo = CommentRepository()


@router.post(
    "/blogs/{blog_id}/comments", response_model=Union[CommentResponse, Error]
)
def create_comment(
    comment: CreateComment,
    repo: CommentRepository = Depends(),
    user: UserResponse = Depends(try_get_jwt_user_data),
):
    """
    [POST] Comment as a logged in user
    """
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please sign in to post a comment",
        )
    post_comment = repo.create_comment(comment, user.user_id)
    if not post_comment:
        raise HTTPException(status_code=400, detail="Unable to post comment")
    return post_comment


# Update a comment
@router.put(
    "/blogs/{blog_id}/comments/{comment_id}",
    response_model=Union[CommentResponse, Error],
)
def update_comment(
    blog_id: int,
    comment_id: int,
    update: CommentUpdate,
    repo: CommentRepository = Depends(),
    user: UserResponse = Depends(try_get_jwt_user_data),
):
    """
    [PUT] Update comment by comment_id
    """
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please sign in to update a comment",
        )
    return repo.update(comment_id, blog_id, update, user.user_id)


@router.delete("/comments/{comment_id}", response_model=bool)
def delete_comment(
    comment_id: int,
    repo: CommentRepository = Depends(),
    user: UserResponse = Depends(try_get_jwt_user_data),
) -> bool:
    """
    [DELETE] comment by comment_id
    """
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sign in to delete comment",
        )
    return repo.delete(comment_id, user.user_id)


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
