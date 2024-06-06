from fastapi import APIRouter, Depends
from queries.comments_queries import CommentRepository

router = APIRouter()
repo = CommentRepository()


@router.delete("/blogs/{blog_id}/comments/{comment_id}")
def delete_comment(
    comment_id: int, repo: CommentRepository = Depends()
) -> bool:
    return repo.delete(comment_id)
