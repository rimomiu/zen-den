from utils.exceptions import BlogDatabaseException
from models.blogs import (
    CreateBlogs,
    BlogResponse,
    Blogs,
    Error,
    BlogUpdate,
    BlogAuthorResponse,
)
import psycopg
from psycopg.rows import class_row
from typing import List, Union
from queries.pool import pool
from models.users import UserAsAuthor


# This function gets the whole list of blogs and
# allows us to get the username of the authors who wrote the blogs
class BlogRepository:
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

    def get_blogs(self) -> Union[Error, List[BlogAuthorResponse]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT b.*, u.username, u.first_name, u.last_name
                        FROM blogs AS b
                        JOIN users AS u
                        ON u.user_id = b.author_id
                        ORDER BY date_published
                        """
                    )
                    result = []
                    for record in db:
                        user = UserAsAuthor(
                            user_id=record[4],
                            username=record[6],
                            first_name=record[7],
                            last_name=record[8],
                        )
                        blog = BlogAuthorResponse(
                            blog_id=record[0],
                            title=record[1],
                            pic_url=record[2],
                            content=record[3],
                            author_id=record[4],
                            date_published=record[5],
                            user=user,
                        )
                        result.append(blog)
                    return result
        except Exception as e:
            print(e)
            return Error("Could not get blogs")

    # This function lets us get a specific blog using blog_id
    def get_blog_by_blog_id(self, blog_id: int) -> Union[BlogResponse, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT * from blogs
                        WHERE blog_id = %s
                        """,
                        [blog_id],
                    )
                    record = db.fetchone()
                    if record:
                        return Blogs(
                            blog_id=record[0],
                            title=record[1],
                            pic_url=record[2],
                            content=record[3],
                            author_id=record[4],
                            date_published=record[5],
                        )
                    else:
                        return Error("Blog not found")

        except Exception:
            return Error("Could not get blog")

    # this function lets us get the list of
    # blogs written by a user using author_id
    def get_blog_by_user_id(self, author_id: int) -> Union[Error, List[Blogs]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT * from blogs
                        WHERE author_id = %s
                        """,
                        [author_id],
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
            return Error("Could not get blog")

    def update(
        self, blog_id: int, blog: BlogUpdate
    ) -> Union[BlogResponse, Error]:
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
                    RETURNING *;
                    """,
                        [blog.title, blog.pic_url, blog.content, blog_id],
                    )
                    updated_blog = db.fetchone()
                    if updated_blog:
                        return BlogResponse(
                            blog_id=updated_blog[0],
                            title=updated_blog[1],
                            pic_url=updated_blog[2],
                            content=updated_blog[3],
                            author_id=updated_blog[4],
                            date_published=updated_blog[5],
                        )
                    else:
                        return Error("Blog not found")
                    # old_blog_data = blog.dict()
                    # return Blogs(id=blog_id, **old_blog_data)
        except Exception as e:
            print(e)
            return Error("Could not update blog")

    def delete(self, blog_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                    DELETE From blogs
                    WHERE blog_id = %s
                    """,
                        [blog_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False
