"""
Callback in Python is a function passed as an argument to another function,
which is then called (or "called back") during the execution of that function.

For function to be called a `callback` it must be:
- passed as argument to another function
- called by that function
"""

from typing import Callable

########## Simple callback ##########


def hello(name: str) -> None:  # callback
    print(f"Hello, {name}!")


def greetings(
    callback: Callable[[str], None],
) -> None:
    callback("Alice")


# `greetings` will call back `hello` function
greetings(callback=hello)

########## Sorting callback ##########


def length(word: str) -> int:  # callback
    return len(word)


words: list[str] = ["banana", "fig", "apple"]
sorted_words = sorted(words, key=length)  # `sorted` is calling back `length`
print(sorted_words)


########## Not a callback ##########


def not_calling(not_callback: Callable[[str], None]) -> None:
    print(not_callback)


not_calling(not_callback=hello)
