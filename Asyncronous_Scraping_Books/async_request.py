import asyncio
import aiohttp
import async_timeout
import time

async def fetch_page(session, url):
    async with async_timeout.timeout(10):
        start = time.time()
        async with session.get(url) as response:
            print(f'{url} took {time.time() - start}')
            return response.status


async def get_multiple_pages(*urls):
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        return await asyncio.gather(*tasks)


if __name__ == '__main__':

    def main():
        urls = ['http://google.com' for i in range(50)]
        start = time.time()
        pages = asyncio.run(get_multiple_pages(*urls))
        print(f'Total took {time.time() - start}')
        for page in pages:
            print(page)

    main()
