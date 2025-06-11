"""
Use asyncio.gather inside async function to run multiple coroutines concurrently.
Waits for all of them to complete.
Returns single coroutine that gathers results in order.
"""

import asyncio
import random


async def download(name: str) -> None:
    print(f"{name} start")
    await asyncio.sleep(random.randint(1, 3))
    print(f"{name} finish")


async def main() -> None:
    await asyncio.gather(download("A"), download("B"), download("C"))


asyncio.run(main())
