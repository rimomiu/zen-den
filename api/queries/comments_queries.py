from models.comments import Comments, Error
from typing import List, Union
from queries.pool import pool


class CommentRepository:
    def get_comments(self) -> Union[Error, List[Comments]]:
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
                        print(record)
                        comment = Comments(
                            comment_id=record[0],
                            body=record[1],
                            blog_id=record[2],
                            author_id=record[3],
                            date_published=record[4],
                        )
                        result.append(comment)
                        print(result)
                    return result
        except Exception as e:
            print(e)
