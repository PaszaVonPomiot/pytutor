"""
Callable is a generic type
"""

from typing import Callable

Callable[[int, int], int]  # [[parameter types], return type]


def sum_ab(a: int, b: int) -> int:
    return a + b


def double(f: Callable[[int, int], int]) -> int:
    return f(2, 3) * 2


double(sum_ab)
