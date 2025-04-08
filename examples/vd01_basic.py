import asyncio
import sys
import os

# Add parent directory to path to import utils
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import async_timer

@async_timer
async def basic_example():
    print("\n--- [1] Basic Async/Await Example ---")
    print("Hello...")
    await asyncio.sleep(3) # Simulate non-blocking I/O
    print("...World!")

if __name__ == "__main__":
    asyncio.run(basic_example())
