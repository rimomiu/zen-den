from utils.exceptions import CommentDatabaseException
from models.comments import (
    Comments,
    Error,
    CreateComment,
    CommentResponse,
    CommentUpdate,
)
import psycopg
from psycopg.rows import class_row

from typing import List, Union
from queries.pool import pool


class CommentRepository:
    def update(
        self,
        comment_id: int,
        blog_id: int,
        comment: CommentUpdate,
        user_id=int,
    ) -> Union[CommentResponse, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                    UPDATE comments
                    SET body = %s
                    WHERE comment_id = %s AND blog_id = %s AND author_id = %s
                    RETURNING *;
                    """,
                        [comment.body, comment_id, blog_id, user_id],
                    )
                    updated_comment = db.fetchone()
                    if updated_comment:
                        return CommentResponse(
                            comment_id=updated_comment[0],
                            body=updated_comment[1],
                            blog_id=updated_comment[2],
                            author_id=updated_comment[3],
                            date_published=updated_comment[4],
                        )
                    else:
                        return Error("Comment not found")
        except psycopg.Error as e:
            print(e)
            return Error("Could not update comment")

    def create_comment(
        self, comment: CreateComment, user_id: int
    ) -> CommentResponse:
        try:
            with pool.connection() as conn:
                with conn.cursor(
                    row_factory=class_row(CommentResponse)
                ) as cur:
                    cur.execute(
                        """
                        INSERT INTO comments (
                        body,
                        blog_id,
                        author_id,
                        date_published
                    ) VALUES (
                        %s, %s, %s, %s
                    )
                    RETURNING *;
                    """,
                        [
                            comment.body,
                            comment.blog_id,
                            user_id,
                            comment.date_published,
                        ],
                    )

                    comment = cur.fetchone()
                    if not comment:
                        raise CommentDatabaseException(
                            "Couldn't create comment"
                        )
        except psycopg.Error as e:
            print(e)
            raise CommentDatabaseException("Couldn't create comment")
        return comment

    def delete(self, blog_id: int, comment_id: int, user_id=int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        DELETE FROM comments
                        WHERE blog_id = %s
                        AND comment_id = %s
                        AND author_id=%s
                        """,
                        [blog_id, comment_id, user_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def get_comments_by_blog_id(
        self, blog_id: int
    ) -> Union[Error, List[Comments]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT * FROM comments
                         WHERE blog_id = %s
                        """,
                        [blog_id],
                    )
                    result = []
                    for record in db:
                        comment = Comments(
                            comment_id=record[0],
                            body=record[1],
                            blog_id=record[2],
                            author_id=record[3],
                            date_published=record[4],
                        )
                        result.append(comment)
                    return result
        except Exception:
            return Error("Could not get comments")

    def get_comments_by_user(
        self, author_id: int
    ) -> Union[Error, List[Comments]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT * FROM comments
                        WHERE author_id = %s
                        """,
                        [author_id],
                    )
                    result = []
                    for record in db:
                        comment = Comments(
                            comment_id=record[0],
                            body=record[1],
                            blog_id=record[2],
                            author_id=record[3],
                            date_published=record[4],
                        )
                        result.append(comment)
                    return result
        except Exception:
            return Error("Could not get comments")
