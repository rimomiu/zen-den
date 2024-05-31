steps = [
    [
        """
        CREATE TABLE blogs (
        blog_id SERIAL PRIMARY KEY,
        title VARCHAR(100) NOT NULL,
        pic_url VARCHAR(100) NOT NULL,
        body VARCHAR(1500) NOT NULL,
        author_id SMALLINT NOT NULL REFERENCES users (user_id)
        );
""",
    """
DROP TABLE blogs;
"""

],
]
