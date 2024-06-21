"""
Unit Tests for Blog endpoints
"""

from main import app
from fastapi.testclient import TestClient
from queries.blogs_queries import BlogRepository
from models.blogs import CreateBlogs, BlogResponse
from routers.blogs_router import try_get_jwt_user_data
from models.users import UserAsAuthor

# from typing import List, Optional


client = TestClient(app)


"""
Unit-Test Base Case
"""


def test_init():
    assert 1 == 1


"""
Unit-Test POST blog
"""


class TestCreateBlogQueries:
    def create_blogs(self, blogs: CreateBlogs, user_id: int) -> BlogResponse:
        blogs = BlogResponse(
            blog_id=8,
            title=blogs.title,
            author_id=user_id,
            pic_url=blogs.pic_url,
            content=blogs.content,
            date_published=blogs.date_published,
        )
        return blogs


def log_in_user():
    return UserAsAuthor(
        user_id=1,
        username="meow",
        first_name="neko",
        last_name="miao",
    )


def test_create_blogs():
    app.dependency_overrides[BlogRepository] = TestCreateBlogQueries

    json_data = {
        "title": "BigYogaButt",
        "author_id": 1,
        "pic_url": "https://youaligned.com/",
        "content": "Big yoga booty requires a lot of yoga",
        "date_published": "2024-05-29",
    }
    expected = {
        "blog_id": 8,
        "title": "BigYogaButt",
        "author_id": 1,
        "pic_url": "https://youaligned.com/",
        "content": "Big yoga booty requires a lot of yoga",
        "date_published": "2024-05-29",
    }

    app.dependency_overrides[try_get_jwt_user_data] = log_in_user
    response = client.post("/blogs", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


class TestDeleteBlogQueries:
    """
    Unit Test DELETE blog
    """

    def delete(self, blog_id: int, user_id: int) -> bool:
        return True


def test_delete_blog():
    app.dependency_overrides[BlogRepository] = TestDeleteBlogQueries
    app.dependency_overrides[try_get_jwt_user_data] = log_in_user

    response = client.delete("/blogs/1/")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() is True
