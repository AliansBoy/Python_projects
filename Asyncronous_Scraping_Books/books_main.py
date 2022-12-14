import asyncio
import time

import aiohttp
import async_timeout
import requests
import logging

from pages.book_page import BookPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('http://books.toscrape.com').content
page = BookPage(page_content)
books = page.books


async def fetch_page(session, url):
    async with async_timeout.timeout(50):
        start = time.time()
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return await response.text()


async def get_multiple_pages(*urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


def main():
    if __name__ == '__main__':
        global page
        urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(1, page.page_count)]
        start = time.time()

        pages = asyncio.run(get_multiple_pages(*urls))
        print(f'Total page request took {time.time() - start}')

        for page_content in pages:
            logger.debug('Create BooksPage from page content.')
            page = BookPage(page_content)
            books.extend(page.books)


main()



# for page_num in range(1, page.page_count):
#     url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
#     page_content = requests.get(url).content
#     page = BookPage(page_content)
#     books.extend(page.books)
