
import sqlite3
from database import create_database, get_connection
from logger_config import logger
from contextlib import closing


def add_book(title):
    create_database()

    if not isinstance(title, str):
        return "Book title must be text."

    if not title.strip():
        logger.warning("Attempted to add an empty book title")
        return "Book title is required."

    if len(title.strip()) > 200:
        logger.warning("Attempted to add a book title that is too long")
        return "Book title is too long."

    try:
        with closing(get_connection()) as connection:
            with connection:
                cursor = connection.cursor()

                cursor.execute(
                    "INSERT INTO books (title) VALUES (?)",
                    (title,)
                )

        logger.info("Book added: %s", title)
        return "Book added successfully!"

    except sqlite3.Error as error:
        logger.error("Database error: %s", error)
        return "Unable to add book due to a database error."
    
def view_books():
    create_database()

    with closing(get_connection()) as connection:
        with connection:
            cursor = connection.cursor()

            cursor.execute("SELECT title FROM books")
            books = [row[0] for row in cursor.fetchall()]

    return books


def search_book(title):
    create_database()

    try:
        with closing(get_connection()) as connection:
            with connection:
                cursor = connection.cursor()

                cursor.execute(
                    "SELECT title FROM books WHERE title LIKE ?",
                    (f"%{title}%",)
                )

                result = cursor.fetchone()

        return result[0] if result else None

    except sqlite3.Error as error:
        logger.error("Database error while searching books: %s", error)
        return None

def remove_book(title):
    create_database()

    try:
        with closing(get_connection()) as connection:
            with connection:
                cursor = connection.cursor()

                cursor.execute(
                    "DELETE FROM books WHERE LOWER(title) = LOWER(?)",
                    (title,)
                )

                removed = cursor.rowcount

        if removed:
            return "Book removed successfully!"

        return "Book not found."

    except sqlite3.Error as error:
        logger.error("Database error while removing book: %s", error)
        return "Unable to remove book due to a database error."