"""
Generic functions use variable types  e.g. "T"
"""

from typing import TypeVar

from mypy.semanal import dummy_context


# Generic function
def first[T](items: list[T]) -> T:
    return items[0]


# Constrained Variable Type
# must be resolved to exactly one type
str_or_int = TypeVar("str_or_int", str, int)


def sum_or_concatenate(a: str_or_int, b: str_or_int) -> str_or_int:
    return a + b


sum_or_concatenate(1, 2)
sum_or_concatenate("a", "b")
