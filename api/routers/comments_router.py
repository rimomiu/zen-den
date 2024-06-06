from fastapi import APIRouter, Depends
from queries.comments_queries import CommentRepository
from models.comments import Comments, Error
from typing import List, Union

router = APIRouter()
repo = CommentRepository()


@router.get("/comments", response_model=Union[Error, List[Comments]])
def get_comments(
    repo: CommentRepository = Depends(),
):
    return repo.get_comments()
