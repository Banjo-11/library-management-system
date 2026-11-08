
import sqlite3
from database import create_database


def add_book(title):
    create_database()

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO books (title) VALUES (?)",
        (title,)
    )

    connection.commit()
    connection.close()

    return "Book added successfully!"


def view_books():
    create_database()

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute("SELECT title FROM books")
    books = [row[0] for row in cursor.fetchall()]

    connection.close()

    return books


def search_book(title):
    create_database()

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT title FROM books WHERE title LIKE ?",
        (f"%{title}%",)
    )

    result = cursor.fetchone()
    connection.close()

    return result[0] if result else None


def remove_book(title):
    create_database()

    connection = sqlite3.connect("library.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM books WHERE LOWER(title) = LOWER(?)",
        (title,)
    )

    removed = cursor.rowcount

    connection.commit()
    connection.close()

    if removed:
        return "Book removed successfully!"

    return "Book not found."
