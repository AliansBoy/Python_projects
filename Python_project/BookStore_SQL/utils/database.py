from typing import List, Dict, Union

from .database_connection import DataBaseConnection

"""
Concerned with storing and retrieving books from a json file

Format of the json file:
[
    {
        'name': Matrix
        'author': Someone
        'read': True
    }
]
"""


def create_book_table() -> None:
    with DataBaseConnection('bookstore.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')


def add_book(name: str, author: str) -> None:
    try:
        with DataBaseConnection('bookstore.db') as connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

            # Wrong way to inserting information, because can be injection attack
            # cursor.execute(f'INSERT INTO books VALUE("{name}", "{author}", 0)')

    except IOError:
        create_book_table()
        add_book(name, author)


def get_books() -> List[Dict[str, Union[str, int]]]:
    try:
        with DataBaseConnection('bookstore.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM books')

            books = [{'name': col[0], 'author': col[1], 'read': col[2]} for col in cursor.fetchall()]
            return books
    except IOError:
        create_book_table()
        get_books()


def read_book(name: str) -> None:
    with DataBaseConnection('bookstore.db') as connection:
        cursor = connection.cursor()
        cursor.execute('Update books SET read=1 WHERE name=?', (name,)) #Using tuple, because needed iterable parameter


def delete_book(name: str) -> None:
    with DataBaseConnection('bookstore.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,)) #Using tuple, because needed iterable parameter


