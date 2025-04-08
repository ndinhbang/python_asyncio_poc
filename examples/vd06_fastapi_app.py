import asyncio
import time
import httpx
from fastapi import FastAPI
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from Asyncio FastAPI POC"}

@app.get("/sleep/{seconds}")
async def sleep_endpoint(seconds: int):
    """
    Simulates an async I/O operation (non-blocking).
    The server can handle other requests while waiting.
    """
    start = time.perf_counter()
    await asyncio.sleep(seconds)
    elapsed = time.perf_counter() - start
    return {"message": f"Slept for {seconds} seconds", "elapsed": elapsed}

@app.get("/blocking")
async def blocking_endpoint():
    """
    WARNING: This blocks the event loop!
    Try opening http://127.0.0.1:8000/ in another tab while this is loading.
    You will see that the other request HANGS until this one finishes.
    """
    print("--> Start BLOCKING request (Server will freeze for 5s)...")
    time.sleep(5)
    print("<-- End BLOCKING request (Server resumes)...")
    return {"message": "I blocked the server for 5 seconds :("}

@app.get("/blocking-fixed")
async def blocking_fixed_endpoint():
    """
    Runs blocking code in a separate thread using asyncio.to_thread.
    The event loop remains free.
    Try opening http://127.0.0.1:8000/ in another tab while this is loading.
    It should respond IMMEDIATELY.
    """
    print("--> Start THREADED request (Server stays alive)...")
    # asyncio.to_thread runs the sync function in a separate thread
    await asyncio.to_thread(time.sleep, 5)
    print("<-- End THREADED request...")
    return {"message": "I slept for 5 seconds without blocking the server :)"}

@app.get("/proxy")
async def proxy_endpoint():
    """
    Demonstrates an async HTTP proxy using httpx.
    Fetches data from an external API asynchronously.
    """
    url = "https://www.google.com"
    print(f"Fetching {url}...")
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)

    return {
        "url": url,
        "status_code": resp.status_code,
        "server_header": resp.headers.get("server"),
        "message": "Fetched successfully using async httpx"
    }

if __name__ == "__main__":
    import uvicorn
    print("Starting FastAPI server on http://127.0.0.1:8000")
    print("Documentation available at http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)
