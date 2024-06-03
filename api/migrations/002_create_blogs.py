steps = [
    [
        """
        CREATE TABLE blogs (
        blog_id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        pic_url VARCHAR(100) NOT NULL,
        content VARCHAR(1500) NOT NULL,
        author_id SMALLINT NOT NULL REFERENCES users (user_id),
        date_published DATE NOT NULL
        );
        """,
        """
        DROP TABLE blogs;
        """
    ],
]
