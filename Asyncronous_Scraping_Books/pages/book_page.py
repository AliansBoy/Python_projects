import re
import logging
from bs4 import BeautifulSoup

from Scraping_Books.locator.book_page_locator import BookPageLocator
from Scraping_Books.parsers.book import BookParser

logger = logging.getLogger('scraping.book_page')


class BookPage:
    def __init__(self, page):
        logger.debug('Parsing page content with BeautifulSoup HTML parser.')
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def books(self):
        logger.debug(f'Finding all books in the page using `{BookPageLocator.BOOKS}`.')
        locator = BookPageLocator.BOOKS
        all_books = self.soup.select(locator)
        return [BookParser(el) for el in all_books]

    @property
    def page_count(self):
        logger.debug('Find all number of catalog pagers available...')
        locator = BookPageLocator.PAGER
        content = self.soup.select_one(locator).string
        logger.info(f'Found number of catalogue pages available: `{content}`.')

        pattern = 'Page [0-9]+ of ([0-9]+)'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages as integer `{pages}`.')
        return pages

