steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            user_id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            username VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(256) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            admin BOOLEAN NOT NULL DEFAULT false
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ],
    [
        # "Up" SQL statement
        """
        INSERT INTO users VALUES
            (1, 'Cody', 'Huls', 'chuls', 'chh57@nau.edu', 'rawrXD'),
            (2, 'Chloe', 'Huls', 'chloie', 'cholow33@gmail.com', 'meow77'),
            (3, 'Savannah', 'Cavnes', 'sav2000', 'beachgirl202@gmail.com', 'hawaii'),
            (4, 'Julia', 'Kleven', 'discodoggie', 'juliagirl@gmail.com', 'woof');
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """
    ]
]
# if we want to add things to this table by creating a new file,
# 004_create_users and do "Alter Table" instead of "Create Table" and icnlude only the alterations you want to include
