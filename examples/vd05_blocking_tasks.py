import asyncio
import time
import concurrent.futures
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import async_timer

def blocking_io(n):
    print(f"Starting blocking IO {n}")
    time.sleep(4) # This is a blocking function, not await
    print(f"Finished blocking IO {n}")
    return f"Result {n}"

@async_timer
async def blocking_tasks_example():
    print("\n--- [5] Blocking Tasks Example ---")
    loop = asyncio.get_running_loop()

    print("Running blocking functions in ThreadPoolExecutor...")
    with concurrent.futures.ThreadPoolExecutor() as pool:
        # loop.run_in_executor runs blocking function in another thread
        # to avoid blocking the main event loop
        tasks = [
            loop.run_in_executor(pool, blocking_io, i)
            for i in range(1, 4)
        ]
        results = await asyncio.gather(*tasks)
        print(f"Result: {results}")

if __name__ == "__main__":
    asyncio.run(blocking_tasks_example())
