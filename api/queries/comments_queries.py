from utils.exceptions import CommentDatabaseException
import psycopg
from queries.pool import pool


class CommentRepository:
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
