"""
Courutine needs to be awaited so it cannot be called directly because it will
give error `RuntimeWarning: coroutine 'main' was never awaited`.
Use `asyncio.run` to run async function in synchronious code.
It will create event loop, run coroutine and close the loop.

async - keyword indicates that function is pausable (on await)
await - means to pause the function and process event loop until awaited
task is complete
"""

import asyncio


async def main() -> None:  # async entrypoint function
    print("Hello")


asyncio.run(main())  # provide entryption as argument
