from fastapi import APIRouter, Depends
from queries.comments_queries import CommentRepository
from models.comments import (
    Comments,
    CreateComment,
    Error,
    CommentResponse,
    CommentUpdate,
)
from typing import List, Union

router = APIRouter()
repo = CommentRepository()


@router.get(
    "/blogs/{blog_id}/comments", response_model=Union[Error, List[Comments]]
)
def list_comments(repo: CommentRepository = Depends()):
    return repo.list_comments()


@router.post("/blogs/{blog_id}/comments", response_model=CommentResponse)
def create_comment(
    comment: CreateComment, repo: CommentRepository = Depends()
):
    return repo.create_comment(comment)


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
    return repo.update(comment_id, blog_id, update)


@router.delete("/blogs/{blog_id}/comments/{comment_id}")
def delete_comment(
    comment_id: int, repo: CommentRepository = Depends()
) -> bool:
    return repo.delete(comment_id)
