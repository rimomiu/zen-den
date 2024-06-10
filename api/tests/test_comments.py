from main import app
from fastapi.testclient import TestClient
from queries.comments_queries import CommentRepository
from models.comments import CommentResponse, CommentUpdate


client = TestClient(app)


"""
Unit-Test Base Case
"""


def test_init():
    assert 1 == 1


"""
Unit-Test GET comments
"""


class EmptyCommentsQueries:
    def list_comments(self):
        return []


def test_get_all_comments():
    app.dependency_overrides[CommentRepository] = EmptyCommentsQueries

    response = client.get("/blogs/{blog_id}/comments")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == []


"""
Unit-Test POST comment
"""


class TestCommentQueries:
    def create_comment(self, comment):
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
        "date_published": "2024-06-06T00:00:00",
    }
    expected = {
        "comment_id": 1,
        "body": "I love yoga, but I can't even touch my toes!",
        "blog_id": 1,
        "author_id": 1,
        "date_published": "2024-06-06T00:00:00",
    }

    response = client.post("/blogs/{blog_id}/comments", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


"""
Unit-Test UPDATE comment
"""


class TestUpdateCommentQueries:
    def update(self, comment_id: int, blog_id: int, update: CommentUpdate):
        return CommentResponse(
            comment_id=comment_id,
            body=update.body,
            blog_id=blog_id,
            author_id=1,
            date_published="2024-06-06T00:00:00",
        )


def test_update_comment():
    app.dependency_overrides[CommentRepository] = TestUpdateCommentQueries

    json_data = {"body": "Updated comment body"}
    expected = {
        "comment_id": 1,
        "body": "Updated comment body",
        "blog_id": 1,
        "author_id": 1,
        "date_published": "2024-06-06T00:00:00",
    }

    response = client.put("/blogs/1/comments/1", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


"""
Unit Test DELETE comment
"""


class TestDeleteCommentQueries:
    def delete(self, comment_id: int) -> bool:
        return True


def test_delete_comment():
    app.dependency_overrides[CommentRepository] = TestDeleteCommentQueries

    response = client.delete("/blogs/1/comments/1")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() is True
