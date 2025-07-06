"""
A dictionary that tracks which keys have been accessed.
"""

from typing import Any


class TrackingDict(dict):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.used_keys = set()

    def __getitem__(self, key) -> Any:
        self.used_keys.add(key)
        return super().__getitem__(key)

    def get_used_keys(self) -> set:
        return self.used_keys


d1 = dict(a=1, b=2, c=3)
d2 = TrackingDict(a=1, b=2, c=3)

print(d1)
print(d2)

d2["b", "c"]
print(d2.get_used_keys())
