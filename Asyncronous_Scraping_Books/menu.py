import logging

from Scraping_Books.books_main import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Enter one of following

- 'b' to look at 5 star books
- 'c' to look at the cheapest books
- 'n' to just get the next available books on the page
- 'x' to exit

Enter your choice:'''


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1) #only first 10
    five_star_books = [el for el in best_books if el.rating == 5]
    for book in five_star_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding best books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10] #only first 10
    for book in cheapest_books:
        print(book)


def cheapest_and_best():
    best_cheap = sorted(books, key=lambda x: (x.rating * -1, x.price))[:5]
    for book in best_cheap:
        print(book)


books_generator = (x for x in books)


def next_book():
    logger.info('Finding next book from generator of all books...')
    print(next(books_generator))


_user_option = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': next_book
}


def menu():
    selection = input(USER_CHOICE)
    while selection != 'x':
        if selection in _user_option:
            selected_function = _user_option[selection]
            selected_function()
        else:
            print("Unknown command, please try again! ")

        selection = input(USER_CHOICE)
    logger.debug('Termination program...')


menu()
