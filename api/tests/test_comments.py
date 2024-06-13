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
    CommentUpdate,
    Error
)
from typing import List, Union


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


"""
******************************************************************
Unit-Test Error Handling
#5 Endpoints => #5 Error Unit Tests
"""


class TestErrorHandlingQueries:
    def get_comments_by_blog_id(self, blog_id: int) -> Union[Error, List[Comments]]:
        raise Exception("Database error")

    def get_comments_by_user(self, author_id: int) -> Union[Error, List[Comments]]:
        raise Exception("Database error")

    def create_comment(self, comment: CreateComment) -> CommentResponse:
        raise Exception("Database error")

    def update(self, comment_id: int, blog_id: int, update: CommentUpdate) -> Union[CommentResponse, Error]:
        raise Exception("Database error")

    def delete(self, comment_id: int) -> bool:
        raise Exception("Database error")


def test_get_blog_comments_error():
    app.dependency_overrides[CommentRepository] = TestErrorHandlingQueries

    response = client.get("/blogs/1/comments")
    app.dependency_overrides = {}

    assert response.status_code == 400
    assert response.json() == {"detail": "Error retrieving"}


def test_get_user_comments_error():
    app.dependency_overrides[CommentRepository] = TestErrorHandlingQueries

    response = client.get("/comments/users/1")
    app.dependency_overrides = {}

    assert response.status_code == 400
    assert response.json() == {"detail": "Error retrieving"}


def test_create_comment_error():
    app.dependency_overrides[CommentRepository] = TestErrorHandlingQueries

    json_data = {
        "body": "Test comment",
        "blog_id": 1,
        "author_id": 1,
        "date_published": "2024-06-06",
    }

    response = client.post("/blogs/1/comments", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 400
    assert response.json() == {"detail": "Error creating comment"}


def test_update_comment_error():
    app.dependency_overrides[CommentRepository] = TestErrorHandlingQueries

    json_data = {"body": "Updated comment body"}

    response = client.put("/blogs/1/comments/1", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 400
    assert response.json() == {"detail": "Error updating comment"}


def test_delete_comment_error():
    app.dependency_overrides[CommentRepository] = TestErrorHandlingQueries

    response = client.delete("/blogs/1/comments/1")
    app.dependency_overrides = {}

    assert response.status_code == 400
    assert response.json() == {"detail": "Error deleting comment"}


"""
******************************************************************
Unit-Test Validation
#2 Pydantic Validation Error => #2 Unit Test [POST],[PUT]
"""


def test_create_comment_validation_error():
    app.dependency_overrides[CommentRepository] = TestCommentQueries

    # Missing required fields
    invalid_data = {
        "body": "I love yoga",
        # "blog_id": 1,
        # "author_id": 1,
        "date_published": "2024-06-06",
    }

    response = client.post("/blogs/1/comments", json=invalid_data)
    app.dependency_overrides = {}

    assert response.status_code == 422  # Unprocessable Entity


def test_update_comment_validation_error():
    app.dependency_overrides[CommentRepository] = TestUpdateCommentQueries

    # Missing required fields
    invalid_data = {}

    response = client.put("/blogs/1/comments/1", json=invalid_data)
    app.dependency_overrides = {}

    assert response.status_code == 422  # Unprocessable Entity


"""
******************************************************************
Unit-Test Boundary Conditions
#1 Boundary => #1 Unit Test
"""

def test_create_comment_empty_body():
    app.dependency_overrides[CommentRepository] = TestCommentQueries

    json_data = {
        "body": "",
        "blog_id": 1,
        "author_id": 1,
        "date_published": "2024-06-06",
    }
    response = client.post("/blogs/1/comments", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json()["body"] == ""


def test_create_comment_large_body():
    app.dependency_overrides[CommentRepository] = TestCommentQueries

    large_body = "a" * 10000  # Very large comment body
    json_data = {
        "body": large_body,
        "blog_id": 1,
        "author_id": 1,
        "date_published": "2024-06-06",
    }
    response = client.post("/blogs/1/comments", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json()["body"] == large_body
