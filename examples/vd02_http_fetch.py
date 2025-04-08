import asyncio
import httpx
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import async_timer

async def fetch_url(client, url):
    print(f"Fetching {url}...")
    await asyncio.sleep(1) # Simulate network latency
    resp = await client.get(url)
    print(f"Fetched {url}: {resp.status_code}")

@async_timer
async def http_fetch_example():
    print("\n--- [2] HTTP Fetch Example ---")
    urls = ["https://www.google.com", "https://www.github.com", "https://www.python.org"]

    async with httpx.AsyncClient() as client:
        print("\n[Sequential]")
        for url in urls:
            await fetch_url(client, url)

        print("\n[Concurrent (gather)]")
        tasks = [fetch_url(client, url) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(http_fetch_example())
