"""
Unit Tests for Blog endpoints
"""

from main import app
from fastapi.testclient import TestClient
from queries.blogs_queries import BlogRepository
from models.blogs import CreateBlogs, BlogUpdate, BlogResponse, Blogs
from typing import List, Optional


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
    def create_blogs(self, blogs: CreateBlogs) -> BlogResponse:
        blogs = BlogResponse(
            blog_id=blogs.blog_id,
            title=blogs.title,
            author_id=blogs.author_id,
            pic_url=blogs.pic_url,
            content=blogs.content,
            date_published=blogs.date_published,
        )
        return blogs


def test_create_blogs():
    app.dependency_overrides[BlogRepository] = TestCreateBlogQueries

    json_data = {
        "title": "BigYogaButt",
        "author_id": 1,
        "pic_url": "https://youaligned.com/wp-content/uploads/2022/11/yoga-poses-for-your-butt.jpg",
        "content": "Big yoga booty requires a lot of yoga",
        "date_published": "2024-05-29",
    }
    expected = {
        "blog_id": 1,
        "title": "BigYogaButt",
        "author_id": 1,
        "pic_url": "https://youaligned.com/wp-content/uploads/2022/11/yoga-poses-for-your-butt.jpg",
        "content": "Big yoga booty requires a lot of yoga",
        "date_published": "2024-05-29",
    }

    response = client.post("/blogs", json=json_data)
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == expected


class TestDeleteBlogQueries:
    """
    Unit Test DELETE blog
    """
    def delete(self, blog_id: int) -> bool:
        return True

def test_delete_blog():
    app.dependency_overrides[BlogRepository] = TestDeleteBlogQueries

    response = client.delete("/blogs/1/")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() is True