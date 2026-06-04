"""
Singleton cached factory.

`functools.cache` stores the result of a function call by its arguments. When a
zero-argument factory is cached, every call uses the same cache key and returns
the same object.

This keeps construction lazy: the singleton is created only when the factory is
called for the first time, instead of at module import time. Import the factory
wherever the object is needed and call it to get the shared instance.
"""

from dataclasses import dataclass
from functools import cache


@dataclass
class Config:
    value: int = 42


@cache
def get_config() -> Config:
    return Config()
