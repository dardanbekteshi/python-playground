import asyncio
import random
import sys
import time

import aiohttp
import requests

def fetch_sync(url:str)-> str:
    res = requests.get(url)
    return res.text

def sync_main()-> None:
    original_url = "https://jsonplaceholder.typicode.com/todos/11"
    slow_url = slow_it(original_url=original_url,delay=DELAY)
    multiple_urls = [slow_url for _ in range(NUMBER_OF_URLS)]
    for url in multiple_urls:
        res = fetch_sync(url)
        print(res)

async def fetch(session:aiohttp.ClientSession, url:str) -> str:
    async with session.get(url) as response:
        res = await response.text()
        return res

async def main()-> None:
    original_url = "https://jsonplaceholder.typicode.com/todos/11"
    slow_url = slow_it(original_url=original_url,delay=DELAY)
    multiple_urls = [slow_url for _ in range(NUMBER_OF_URLS)]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session=session,url=uu) for uu in multiple_urls]
        results = await asyncio.gather(*tasks)
        print(results)

def slow_it(original_url:str,delay:int) -> str:
    slow_url = f"http://slowwly.robertomurray.co.uk/delay/{delay * 1000}/url/{original_url}"
    return slow_url

if __name__ == "__main__":
    _, mode, ulrs, delay = sys.argv
    NUMBER_OF_URLS = int(ulrs)
    DELAY = int(delay)

    if mode == "sync":
        sync_main()
    elif mode == "async":
        asyncio.run(main())
    else:
        sys.exit("specify a mode from [async,sync]")
