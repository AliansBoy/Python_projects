import json

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



books_file = 'book.txt'


def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)


def add_book(name, author):
    books = get_books()
    books.append({'name': name, 'author': author, 'read': False})
    _save_all_books(books)


def get_books():
    try:
        with open(books_file, 'r') as file:
            return json.load(file)
    except IOError:
        create_book_table()
        get_books()


def read_book(name):
    books = get_books()
    for book in books:
        if book['name'] == name:
            book['read'] = 'True'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)


def delete_book(name):
    books = get_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

