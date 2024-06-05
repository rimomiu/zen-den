from utils.exceptions import BlogDatabaseException
from models.blogs import CreateBlogs, BlogResponse, Blogs, Error
import psycopg
from psycopg.rows import class_row
from typing import List, Union
from queries.pool import pool


# class Blogs(BaseModel):
#     title: str
#     pic_url: str
#     content: str
#     author_id: int


class BlogRepository:
    def get_blogs(self) -> Union[Error, List[Blogs]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT * FROM blogs
                        ORDER BY date_published
                        """
                    )
                    result = []
                    for record in db:
                        blog = Blogs(
                            blog_id=record[0],
                            title=record[1],
                            pic_url=record[2],
                            content=record[3],
                            author_id=record[4],
                            date_published=record[5],
                        )
                        result.append(blog)
                    return result

        except Exception:
            return Error("Could not get blogs")

    def update(self, blog_id: int, blog: Blogs) -> Union[Blogs, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                    UPDATE blogs
                    SET title = %s
                    , pic_url = %s
                    , content = %s
                    WHERE blog_id = %s
                    """,
                        [blog.title, blog.pic_url, blog.content, blog_id],
                    )
                    old_blog_data = blog.dict()
                    return Blogs(id=blog_id, **old_blog_data)
        except Exception as e:
            print(e)
            return Error("Could not update blog")

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
