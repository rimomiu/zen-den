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
        INSERT INTO users (first_name, last_name, username, password, email) VALUES
            ('Cody', 'Huls', 'chuls', 'rawrXD', 'chh57@nau.edu'),
            ('Chloe', 'Huls', 'chloie', 'meow77', 'cholow33@gmail.com'),
            ('Savannah', 'Cavnes', 'sav2000', 'hawaii', 'beachgirl202@gmail.com'),
            ('Julia', 'Kleven', 'discodoggie', 'woof', 'juliagirl@gmail.com');
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        """,
    ],
]
# if we want to add things to this table by creating a new file,
# 004_create_users and do "Alter Table" instead of "Create Table" and icnlude only the alterations you want to include
