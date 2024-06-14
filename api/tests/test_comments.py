"""
******************************************************************
Unit-Tests for main CRUD operations for comments
#5 Endpoints => #5 Unit Tests + #1 Base Case
"""
from main import app
from fastapi.testclient import TestClient
from queries.comments_queries import CommentRepository
from models.comments import (
    CommentResponse,
    CreateComment,
    Comments,
    CommentUpdate
)
from typing import List


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


class TestCommentQueries:
    """
    Unit-Test POST a comment
    """
    def create_comment(self, comment: CreateComment) -> CommentResponse:
        comment = CommentResponse(
            comment_id=1,
            body=comment.body,
            blog_id=comment.blog_id,
            author_id=comment.author_id,
            date_published=comment.date_published,
        )
        return comment


def test_create_comment():
    app.dependency_overrides[CommentRepository] = TestCommentQueries

    json_data = {
        "body": "I love yoga, but I can't even touch my toes!",
        "blog_id": 1,
        "author_id": 1,
        "date_published": "2024-06-06",
    }
    expected = {
        "comment_id": 1,
        "body": "I love yoga, but I can't even touch my toes!",
        "blog_id": 1,
        "author_id": 1,
        "date_published": "2024-06-06",
    }

    response = client.post("/blogs/1/comments", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


class TestUpdateCommentQueries:
    """
    Unit-Test UPDATE comment
    """
    def update(
        self, comment_id: int, blog_id: int, update: CommentUpdate
    ) -> CommentResponse:
        return CommentResponse(
            comment_id=comment_id,
            body=update.body,
            blog_id=blog_id,
            author_id=1,
            date_published="2024-06-06",
        )


def test_update_comment():
    app.dependency_overrides[CommentRepository] = TestUpdateCommentQueries

    json_data = {"body": "Updated comment body"}
    expected = {
        "comment_id": 1,
        "body": "Updated comment body",
        "blog_id": 1,
        "author_id": 1,
        "date_published": "2024-06-06",
    }

    response = client.put("/blogs/1/comments/1", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


class TestDeleteCommentQueries:
    """
    Unit Test DELETE comment
    """
    def delete(self, comment_id: int) -> bool:
        return True


def test_delete_comment():
    app.dependency_overrides[CommentRepository] = TestDeleteCommentQueries

    response = client.delete("/blogs/1/comments/1")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() is True
