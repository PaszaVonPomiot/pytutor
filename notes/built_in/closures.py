"""
A closure is an inner function that carries state from outer function
after outer function has finished

Create a closure in 3 steps:
1. Define a function inside another function.
2. The inner function refers to variables from the outer function.
3. The outer function returns the inner function.
"""

from typing import Callable


# Basic example of closure
def outer() -> Callable:
    """Returns inner function"""
    x = 2

    def inner(y: int) -> int:
        """Returns result, where x is from outer function"""
        return x + y

    return inner
