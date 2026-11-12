import sqlite3
import book_manager


def setup_function():
    connection = sqlite3.connect("library.db")
    connection.execute("DELETE FROM books")
    connection.commit()
    connection.close()


def test_add_book():
    result = book_manager.add_book("Things Fall Apart")

    assert result == "Book added successfully!"
    assert book_manager.view_books() == ["Things Fall Apart"]


def test_view_empty_library():
    assert book_manager.view_books() == []


def test_add_multiple_books():
    book_manager.add_book("Things Fall Apart")
    book_manager.add_book("The Alchemist")

    assert book_manager.view_books() == [
        "Things Fall Apart",
        "The Alchemist"
    ]


def test_search_book():
    book_manager.add_book("Things Fall Apart")

    result = book_manager.search_book("things")

    assert result == "Things Fall Apart"


def test_remove_book():
    book_manager.add_book("Things Fall Apart")

    result = book_manager.remove_book("Things Fall Apart")

    assert result == "Book removed successfully!"
    assert book_manager.view_books() == []


def test_remove_nonexistent_book():
    result = book_manager.remove_book("Unknown Book")

    assert result == "Book not found."


def test_add_empty_book():
    result = book_manager.add_book("")

    assert result == "Book title is required."
    assert book_manager.view_books() == []


def test_add_whitespace_book():
    result = book_manager.add_book("   ")

    assert result == "Book title is required."
    assert book_manager.view_books() == []


def test_add_long_book_title():
    title = "A" * 201

    result = book_manager.add_book(title)

    assert result == "Book title is too long."
    assert book_manager.view_books() == []
