from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


from Scraping_quotes_JS.locator.quote_page_locators import QuotePageLocators
from Scraping_quotes_JS.parsers.quote import QuoteParser


class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        locator = QuotePageLocators.QUOTE
        return [QuoteParser(e) for e in self.browser.find_elements(By.CSS_SELECTOR, locator)]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tag_dropdown(self) -> Select:
        element = self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.TAG_DROPDOWN)
        return Select(element)

    @property
    def search_button(self):
        return self.browser.find_element(By.CSS_SELECTOR, QuotePageLocators.SUBMIT_BUTTON)

    def select_author(self, author_name: str):
        self.author_dropdown.select_by_visible_text(author_name)

    def get_available_tag(self, author_name: str) -> List[str]:
        try:
            self.select_author(author_name)
        except NoSuchElementException as e:
            print(e)
        return [option.text.strip() for option in self.tag_dropdown.options]

    def select_tag(self, tag_name: str):
        self.tag_dropdown.select_by_visible_text(tag_name)

    def search_for_quotes(self, author: str, tag: str) -> List[QuoteParser]:
        self.select_author(author)

        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, QuotePageLocators.TAG_DROPDOWN_VALUE_OPTION)
            )
        )

        try:
            self.select_tag(tag)
        except NoSuchElementException as e:
            print(e)
        self.search_button.click()
        return self.quotes
