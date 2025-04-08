import asyncio
import httpx
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import async_timer

async def fetch_with_sem(sem, client, url):
    # Only allow max N tasks to enter this block at once
    async with sem:
        print(f"Fetching {url}...")
        await asyncio.sleep(2) # Simulate long processing to see Semaphore effect
        resp = await client.get(url)
        print(f"Done {url}: {resp.status_code}")

@async_timer
async def limited_concurrency_example():
    print("\n--- [3] Limited Concurrency Example ---")
    sem = asyncio.Semaphore(2) # Limit 2 concurrent requests
    urls = [
        "https://www.google.com", "https://www.github.com", "https://www.python.org",
        "https://www.google.com", "https://www.github.com", "https://www.python.org"
    ]

    async with httpx.AsyncClient() as client:
        tasks = [fetch_with_sem(sem, client, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(limited_concurrency_example())
