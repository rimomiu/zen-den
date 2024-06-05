from models.blogs import CreateBlogs, BlogResponse
import os
import psycopg
from psycopg_pool import ConnectionPool
from psycopg.rows import class_row

# from typing import Optional
from utils.exceptions import BlogDatabaseException

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

pool = ConnectionPool(DATABASE_URL)


class BlogQueries:
    def create_blogs(self, blogs: CreateBlogs) -> BlogResponse:
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(BlogResponse)) as cur:
                    cur.execute(
                        """
                        INSERT INTO blogs (
                            title,
                            author_id,
                            pic_url,
                            content,
                            date_published
                        ) VALUES (
                            %s, %s, %s, %s, %s
                        )
                        RETURNING *;
                        """,
                        [
                            blogs.title,
                            blogs.author_id,
                            blogs.pic_url,
                            blogs.content,
                            blogs.date_published,
                        ],
                    )

                    blogs = cur.fetchone()
                    if not blogs:
                        raise BlogDatabaseException("Couldn't create blogs")
        except psycopg.Error as e:
            print(e)
            raise BlogDatabaseException("Couldn't create blogs")
        return blogs
