import sqlite3

def get_connection():
    return sqlite3.connect("library.db")

def create_database():
    connection = sqlite3.connect("library.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


create_database()
