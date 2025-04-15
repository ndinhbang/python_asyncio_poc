# Python Asyncio POC with uv

Proof of Concept (POC) project to learn about `asyncio` in Python 3.12, managed by `uv`.

## Requirements
- Install [uv](https://github.com/astral-sh/uv).

## Installation
Run the following command to install dependencies:
```bash
uv sync
```

## Usage
Run `main.py` to open the example selection menu:
```bash
uv run main.py
```

## Examples
1. **Basic**: Demonstrates basic `async`/`await` syntax.
2. **HTTP Fetch**: Compares sequential and concurrent data fetching using `httpx`.
3. **Limited Concurrency**: Uses `asyncio.Semaphore` to limit the number of concurrent requests (avoids server overload/blocking).
4. **Task Group**: Demo `asyncio.TaskGroup` (Python 3.11+) - a safer way to manage tasks, automatically cancelling remaining tasks if one fails.
5. **Blocking Tasks**: How to handle heavy tasks (blocking I/O, computation) using `ThreadPoolExecutor` to avoid freezing the async program.
6. **FastAPI App**: A simple web server demonstrating async endpoints, blocking vs non-blocking operations, and async HTTP proxying.
