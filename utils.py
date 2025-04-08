import time
import functools
from typing import Callable, Any, Awaitable

def async_timer(func: Callable[..., Awaitable[Any]]) -> Callable[..., Awaitable[Any]]:
    """Decorator to measure execution time of async functions."""
    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"\n--- Starting {func.__name__} ---")
        start_time = time.perf_counter()
        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            print(f"--- Finished {func.__name__} in {elapsed:.4f} seconds ---")
    return wrapper
