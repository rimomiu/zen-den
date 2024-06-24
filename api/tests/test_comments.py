"""
******************************************************************
Unit-Tests for main CRUD operations for comments
"""

from main import app
from fastapi.testclient import TestClient
from queries.comments_queries import CommentRepository
from models.users import UserAsAuthor
from models.comments import (
    Comments,
)
from typing import List
from routers.blogs_router import try_get_jwt_user_data


client = TestClient(app)


def test_init():
    """
    Unit-Test Base Case
    """
    assert 1 == 1


class TestGetUserCommentsQueries:
    """
    Unit-Test [GET] user comments
    """

    def get_comments_by_user(self, author_id: int) -> List[Comments]:
        return [
            Comments(
                comment_id=1,
                body="First comment lol",
                blog_id=1,
                author_id=author_id,
                date_published="2024-06-06",
            )
        ]


def test_get_user_comments():
    app.dependency_overrides[CommentRepository] = TestGetUserCommentsQueries

    expected = [
        {
            "comment_id": 1,
            "body": "First comment lol",
            "blog_id": 1,
            "author_id": 1,
            "date_published": "2024-06-06",
        }
    ]

    response = client.get("/comments/users/1")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


class TestGetBlogCommentsQueries:
    """
    Unit-Test [GET] blog comments
    """

    def get_comments_by_blog_id(self, blog_id: int) -> List[Comments]:
        return [
            Comments(
                comment_id=1,
                body="First comment lol",
                blog_id=blog_id,
                author_id=1,
                date_published="2024-06-06",
            )
        ]


def test_get_blog_comments():
    app.dependency_overrides[CommentRepository] = TestGetBlogCommentsQueries

    expected = [
        {
            "comment_id": 1,
            "body": "First comment lol",
            "blog_id": 1,
            "author_id": 1,
            "date_published": "2024-06-06",
        }
    ]

    response = client.get("/blogs/1/comments/")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


def log_in_user():
    return UserAsAuthor(
        user_id=5,
        username="bobo",
        first_name="Bobo",
        last_name="Bobsen",
    )


class TestDeleteCommentQueries:
    """
    Unit Test DELETE comment
    """

    def delete(self, comment_id: int, user_id: int) -> bool:
        return True


def test_delete_comment():
    app.dependency_overrides[CommentRepository] = TestDeleteCommentQueries
    app.dependency_overrides[try_get_jwt_user_data] = log_in_user

    response = client.delete("/comments/3/")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() is True
