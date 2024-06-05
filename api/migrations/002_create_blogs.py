steps = [
    [
        # "Up" SQL statement
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
        # "Down" SQL statement

        """
        DROP TABLE blogs;
        """,
    ],
    [
        # "Up" SQL statement
        """
        INSERT INTO blogs VALUES
            (1, 'BigYogaButt', 'https://youaligned.com/wp-content/uploads/2022/11/yoga-poses-for-your-butt.jpg', 'Big yoga booty requires a lot of yoga', 1, '2024-05-29'),
            (2, 'TheWorldNeedsYoga', 'https://insightssuccess.in/wp-content/uploads/2020/06/World-Yoga-Day-5-fitness-apps.jpg', 'The world needs yoga', 2,  '2024-06-29');
        """,
        # "Down" SQL statement
        """
        DROP TABLE blogs;
        """
    ]
]
