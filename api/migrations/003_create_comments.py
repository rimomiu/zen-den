steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE comments (
            comment_id SERIAL PRIMARY KEY,
            body VARCHAR(50) NOT NULL,
            blog_id INT NOT NULL REFERENCES blogs (blog_id),
            author INT NOT NULL REFERENCES users (user_id)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE comments;
        """
    ],
]
