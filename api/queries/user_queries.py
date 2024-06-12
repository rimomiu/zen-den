"""
Database Queries for Users
"""

import os
import psycopg
from psycopg_pool import ConnectionPool
from psycopg.rows import class_row
from typing import Optional, List
from models.users import UserWithPw, UserRequest, UserUpdate
from utils.exceptions import UserDatabaseException

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

pool = ConnectionPool(DATABASE_URL)


class UserQueries:
    """
    Class containing queries for the Users table

    Can be dependency injected into a route like so

    def my_route(userQueries: UserQueries = Depends()):
        # Here you can call any of the functions to query the DB
    """

    def get_by_username(self, username: str) -> Optional[UserWithPw]:
        """
        Gets a user from the database by username

        Returns None if the user isn't found
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserWithPw)) as cur:
                    cur.execute(
                        """
                            SELECT
                                *
                            FROM users
                            WHERE username = %s
                            """,
                        [username],
                    )
                    user = cur.fetchone()
                    if not user:
                        return None
        except psycopg.Error as e:
            print(e)
            raise UserDatabaseException(f"Error getting user {username}")
        return user

    def get_by_id(self, user_id: int) -> Optional[UserWithPw]:
        """
        Gets a user from the database by user ID

        Returns None if the user isn't found
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserWithPw)) as cur:
                    cur. execute(
                        """
                            SELECT
                                *
                            FROM users
                            WHERE user_id = %s
                            """,
                        [user_id],
                    )
                    user = cur.fetchone()
                    if not user:
                        return None
        except psycopg.Error as e:
            print(e)
            raise UserDatabaseException(f"Error getting user by ID {user_id}")
        return user

    def create_user(
        self, new_user: UserRequest, hashed_password: str
    ) -> UserWithPw:
        """
        Creates a new user in the database

        Raises a UserInsertionException if creating the user fails
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserWithPw)) as cur:
                    cur.execute(
                        """
                        INSERT INTO users (
                            username,
                            password,
                            first_name,
                            last_name,
                            email
                        ) VALUES (
                            %s, %s, %s, %s, %s
                        )
                        RETURNING *;
                        """,
                        [
                            new_user.username,
                            hashed_password,
                            new_user.first_name,
                            new_user.last_name,
                            new_user.email,
                        ],
                    )
                    user = cur.fetchone()
                    if not user:
                        raise UserDatabaseException(
                            f"Couldn't create username {new_user.username}"
                        )
        except psycopg.Error as e:
            print(e)
            raise UserDatabaseException(
                f"Couldn't create username {new_user.username}"
            )
        return user

    def delete_user(self, username: str) -> str:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            DELETE from users
                            WHERE username = %s
                            """,
                        [username],
                    )
                    return f"Deleted profile of {username}"
        except Exception as e:
            print(e)
            return "Could not delete"

    def list_all_users(self) -> List[UserWithPw]:
        """
        Get a list of all users in the database
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserWithPw)) as cur:
                    cur.execute(
                        """
                            SELECT
                                *
                            FROM users
                            ORDER BY username
                            """
                    )
                    users = cur.fetchall()
        except psycopg.Error as e:
            print(e)
            raise UserDatabaseException("Error listing users")
        return users

    def update_user(
        self, username: str, email: str, user_id: int
    ) -> Optional[UserUpdate]:
        """
        Update a user
        """
        try:
            with pool.connection() as conn:
                with conn.cursor(row_factory=class_row(UserUpdate)) as cur:
                    cur.execute(
                        """
                        UPDATE users
                        SET username=%s, email=%s
                        WHERE user_id = %s
                        RETURNING *;
                        """,
                        (username, email, user_id),
                    )
                    user = cur.fetchone()
                    if not user:
                        return None
        except psycopg.Error as e:
            print(e)
            raise UserDatabaseException("Error updating the user")
        return user
