import re
import logging
from Scraping_Books.locator.book_locator import BookLocator

logger = logging.getLogger('scraping.book')

class BookParser:

    RATING = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        logger.debug(f'New book parser created from `{parent}`.')
        self.parent = parent

    def __repr__(self):
        return f'<Name: "{self.name}", Rating: {self.rating}, Price: {self.price}, Link: {self.link}>'

    @property
    def rating(self):
        logger.debug('Finding book rating...')
        locator = BookLocator.RATING
        rating_tag = self.parent.select_one(locator).attrs['class']
        rating_classes = [r for r in rating_tag if r != 'star-rating']
        rating_number = BookParser.RATING.get(rating_classes[0], 'No rating')  # "No rating" if not found
        logger.debug(f'Found book rating, `{rating_number}`.')
        return rating_number

    @property
    def link(self):
        logger.debug('Finding book link...')
        locator = BookLocator.LINK
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found book link, `{item_link}`.')
        return item_link

    @property
    def name(self):
        logger.debug('Finding book name...')
        locator = BookLocator.NAME
        item_name = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found book name, `{item_name}`.')
        return item_name

    @property
    def price(self):
        logger.debug('Finding book price...')
        locator = BookLocator.PRICE
        item_price = self.parent.select_one(locator).string  # £51.77

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f'Found book price, `{float_price}`.')
        return float_price
