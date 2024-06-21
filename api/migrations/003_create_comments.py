steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE comments (
            comment_id SERIAL PRIMARY KEY,
            body VARCHAR(50) NOT NULL,
            blog_id INT NOT NULL REFERENCES blogs (blog_id) ON DELETE CASCADE,
            author_id INT NOT NULL REFERENCES users (user_id) ON DELETE CASCADE,
            date_published DATE NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE comments;
        """,
    ],
    [
        # "Up" SQL statement
        """
        INSERT INTO comments (body, blog_id, author_id, date_published) VALUES
            ('I need this in my life!', 1, 1, '2024-05-30'),
            ('No way, the world needs Tai Chi insted!', 1, 1, '2024-06-30');
        """,
        # "Down" SQL statement
        """
        DROP TABLE comments;
        """,
    ],
]
