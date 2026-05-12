"""
Iterators provide lazy, one-value-at-a-time iteration over iterable.
Class based iterators require:
- __iter__() and __next__() implementation
- manual state management
- StopIteration handling

Generator functions can express the same logic in plain Python functions using yield.
"""

from typing import Self


class SingleUseNumbersIterator:
    """
    Single-pass iterable that returns self-iterator that will
    be exhaused and cannot be reused.
    """

    def __init__(self, start: int, stop: int) -> None:
        self._current = start
        self._stop = stop

    def __iter__(self) -> Self:
        """Return the iterator itself."""
        return self

    def __next__(self) -> int:
        """Return the next number."""

        if self._current >= self._stop:
            raise StopIteration
        value = self._current
        self._current += 1
        return value


class NumbersIterator:
    """Iterator needs both __iter__ and __next__ to adhere to iterator protocol."""

    def __init__(self, start: int, stop: int) -> None:
        self._current = start
        self._stop = stop

    def __iter__(self) -> Self:
        """Return the iterator itself."""
        return self

    def __next__(self) -> int:
        """Return the next number."""
        if self._current >= self._stop:
            raise StopIteration
        value = self._current
        self._current += 1
        return value


class NumbersIterable:
    """Multi-pass iterable that returns new iterator and can be reused."""

    def __init__(self, start: int, stop: int) -> None:
        self._start = start
        self._stop = stop

    def __iter__(self) -> NumbersIterator:
        """Return a new iterator."""
        return NumbersIterator(start=self._start, stop=self._stop)
