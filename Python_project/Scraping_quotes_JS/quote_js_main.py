from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.quote_page import QuotePage



service = Service("D:\Install\chromedriver.exe")
chrome = webdriver.Chrome(service=service)
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotePage(chrome)

try:
    author = input("Enter the author you'd like quotes from: ")
    available_tags = page.get_available_tag(author)
    print("Select one of these tags: [{}]".format(" | ".join(available_tags)))
    tag = input("Enter your tag: ")
except Exception as e:
    print(e)
else:
    print(page.search_for_quotes(author, tag))

"""
author = input("Enter the author you'd like quotes from: ")
page.select_author(author)

tags = page.get_available_tag()
print("Select one of these tags: [{}]".format(" | ".join(tags)))
selected_tag = input("Enter your tag: ")

page.select_tag(selected_tag)
page.search_button.click()

print(page.quotes)
____________#Using program without Encapsulation_____________
"""
