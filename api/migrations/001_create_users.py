steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL NOT NULL UNIQUE,
            first TEXT NOT NULL,
            last TEXT NOT NULL,
            avatar TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            username TEXT NOT NULL UNIQUE,
            referrer_id INTEGER REFERENCES users("id") ON DELETE CASCADE
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
        CREATE TABLE trucks (
            id SERIAL NOT NULL UNIQUE,
            name TEXT NOT NULL,
            website TEXT NOT NULL,
            category TEXT NOT NULL check(category = 'American' or category = 'Asian' or category = 'French' or category = 'Mediterranean' or category = 'Indian' or category = 'Italian' or category = 'Latin'),
            vegetarian_friendly BOOLEAN NOT NULL,
            owner_id INTEGER NOT NULL REFERENCES users("id") ON DELETE CASCADE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE trucks;
        """,
    ],
    [
        # "Up" SQL statement
        """
        CREATE TABLE menu_items (
            id SERIAL NOT NULL UNIQUE,
            name TEXT NOT NULL,
            calories INTEGER NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE menu_items;
        """,
    ],
    [
        # "Up" SQL statement
        """
CREATE TABLE reviews (
    id SERIAL NOT NULL UNIQUE,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    reviewer_id INTEGER REFERENCES users("id") ON DELETE CASCADE,
    rating INTEGER NOT NULL check(rating = 1 or rating = 2 or rating = 3 or rating = 4 or rating = 5),
    truck_id INTEGER NOT NULL REFERENCES trucks("id") ON DELETE CASCADE
);
        """,
        # "Down" SQL statement
        """
        DROP TABLE reviews;
        """,
    ],
    [
        # "Up" SQL statement
        """
CREATE TABLE truck_menu_items (
    truck_id INTEGER NOT NULL REFERENCES trucks("id") ON DELETE CASCADE,
    menu_item_id INTEGER NOT NULL REFERENCES menu_items("id") ON DELETE CASCADE,
    price INTEGER NOT NULL
);
        """,
        # "Down" SQL statement
        """
        DROP TABLE truck_menu_items;
        """,
    ],
]
