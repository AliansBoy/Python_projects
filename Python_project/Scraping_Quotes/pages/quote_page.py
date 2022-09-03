from bs4 import BeautifulSoup

from Scraping_Quotes.locators.quote_page_locators import QuotePageLocators
from Scraping_Quotes.parsers.quote import QuoteParser


class QuotePage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotePageLocators.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]
