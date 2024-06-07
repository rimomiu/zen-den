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
    def get_comment(self) -> Union[Error, List[Comments]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT * FROM comments
                        ORDER BY date_published
                        """
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

        except Exception as e:
            print(e)
            return Error("Could not get comments")

    def update(
        self, comment_id: int, blog_id: int, comment: CommentUpdate
    ) -> Union[CommentResponse, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                    UPDATE comments
                    SET body = %s
                    WHERE comment_id = %s AND blog_id = %s
                    RETURNING *;
                    """,
                        [comment.body, comment_id, blog_id],
                    )

                    updated_comment = db.fetchone()
                    print(updated_comment)
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

    def create_comment(self, comment: CreateComment) -> CommentResponse:
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
                            comment.author_id,
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

    def delete(self, comment_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        DELETE FROM comments WHERE comment_id = %s
                        """,
                        [comment_id],
                    )
                    if cur.rowcount == 0:
                        raise CommentDatabaseException(
                            "Can't find this comment"
                        )
        except psycopg.Error as e:
            print(e)
            raise CommentDatabaseException("Couldn't find this comment")
        return True
