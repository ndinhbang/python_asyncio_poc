import asyncio
import sys

# Import examples
try:
    from examples.vd01_basic import basic_example
    from examples.vd02a_http_fetch_sequential import http_fetch_sequential_example
    from examples.vd02b_http_fetch_concurrent import http_fetch_concurrent_example
    from examples.vd03_limited_concurrency import limited_concurrency_example
    from examples.vd04_task_group import task_group_example
    from examples.vd05_blocking_tasks import blocking_tasks_example
    # vd06 is run as a subprocess, so no import needed here
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure the 'examples' directory exists and has the correct structure.")
    sys.exit(1)

async def main():
    while True:
        print("\n=== Python Asyncio POC Runner ===")
        print("1. Basic (Basic Async/Await)")
        print("2a. HTTP Fetch (Sequential)")
        print("2b. HTTP Fetch (Concurrent)")
        print("3. Limited Concurrency (Semaphore)")
        print("4. Task Group (Structured Concurrency)")
        print("5. Blocking Tasks (ThreadPoolExecutor)")
        print("6. FastAPI App (Async Web Server)")
        print("0. Exit")

        choice = input("Select example (0-6): ")

        if choice == '0':
            print("Goodbye!")
            break

        try:
            if choice == '1': await basic_example()
            elif choice == '2a': await http_fetch_sequential_example()
            elif choice == '2b': await http_fetch_concurrent_example()
            elif choice == '3': await limited_concurrency_example()
            elif choice == '4': await task_group_example()
            elif choice == '5': await blocking_tasks_example()
            elif choice == '6':
                print("\n--- [6] FastAPI App Example ---")
                print("Launching FastAPI server...")
                print("Press Ctrl+C to stop the server and return to menu.")
                # Run the FastAPI app in a subprocess
                proc = await asyncio.create_subprocess_exec(
                    sys.executable, "examples/vd06_fastapi_app.py",
                )
                try:
                    await proc.wait()
                except asyncio.CancelledError:
                    proc.terminate()
                    await proc.wait() # Ensure process is cleaned up
            else: print("Invalid choice.")
        except Exception as e:
            print(f"An error occurred: {e}")

        await asyncio.sleep(0.5)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, EOFError):
        print("\nExited.")
