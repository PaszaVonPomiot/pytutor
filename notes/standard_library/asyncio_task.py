"""
asyncio.create_task() creates Task object and schedules it in the event loop.
Use create_task() for control, background scheduling, and flexibility.

"""

import asyncio


async def worker(name: str, delay: float) -> None:
    print(f"{name} started")
    await asyncio.sleep(delay)
    print(f"{name} finished")


async def main() -> None:
    """
    During await only current coroutine is paused,
    event loop continues to work.
    t = 0s   → Task A and B both start
    t = 1s   → Task B finishes (prints "Task B finished")
    t = 3s   → Task A finishes (prints "Task A finished")
    """
    task1 = asyncio.create_task(worker("Task A", 3))
    task2 = asyncio.create_task(worker("Task B", 1))
    print("Both tasks running...")
    await task1  # synchronioush code waits for task1 to complete
    await task2  # task2 has already finished during task1 await


asyncio.run(main())
