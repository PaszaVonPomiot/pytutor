"""
A dictionary that tracks which keys have been accessed.
"""

from typing import TypeVar

K = TypeVar("K")
V = TypeVar("V")


class TypedTrackingDict(dict[K, V]):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.used_keys: set[K] = set()

    def __getitem__(self, key: K) -> V:
        self.used_keys.add(key)
        return super().__getitem__(key)

    def get_used_keys(self) -> set[K]:
        return self.used_keys


d1 = dict(a=1, b=2, c=3)
d2 = TypedTrackingDict[str, int](a=1, b=2, c=3)

d2["b"]

print(d1)
print(d2)

print(d2.get_used_keys())
