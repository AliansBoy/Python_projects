"""
Concerned with storing and retrieving books from a list
"""
books = []


def add_book(name, author):
    books.append({"name": name, "author": author, "read": False})


def get_books():
    return books


def read_book(name):
    for book in books:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    global books
    books = [book for book in books if book['name'] != name]

#def delete_book(name):
#   for book in books:
#        if book["name"] == name:
#           books.remove(book)
#        else:
#            print("This book doesn't exist")
