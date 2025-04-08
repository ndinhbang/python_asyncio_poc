import asyncio
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import async_timer

async def task_that_fails():
    await asyncio.sleep(2)
    raise ValueError("Simulated error!")

async def task_that_succeeds():
    try:
        await asyncio.sleep(4)
        print("Success task (will never be printed if cancelled)")
    except asyncio.CancelledError:
        print("Success task was CANCELLED because another task failed!")
        raise

@async_timer
async def task_group_example():
    print("\n--- [4] Task Group Example ---")
    print("Starting TaskGroup...")
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(task_that_succeeds())
            tg.create_task(task_that_fails())
    except ExceptionGroup as eg:
        print(f"\nCaught ExceptionGroup: {eg}")
        print("Note: TaskGroup automatically cancels remaining tasks when one fails.")

if __name__ == "__main__":
    asyncio.run(task_group_example())
