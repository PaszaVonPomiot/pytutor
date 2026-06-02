from dataclasses import dataclass
from typing import ClassVar

examples = {
    "bool": (True, "immutable, truth values"),
    "int": (42, "immutable, whole numbers"),
    "float": (3.14, "immutable, decimal numbers"),
    "complex": (2 + 1j, "immutable, real + imaginary"),
    "str": ("hello", "immutable, text"),
    "list": ([1, 2, 3], "mutable, ordered"),
    "tuple": ((1, 2, 3), "immutable, ordered"),
    "range": (range(3), "immutable, integer sequence"),
    "dict": ({"a": 1, "b": 2}, "mutable, key-value mapping"),
    "set": ({1, 2, 3}, "mutable, unique values"),
    "frozenset": (frozenset({1, 2, 3}), "immutable, unique values"),
    "bytes": (b"abc", "immutable, binary data"),
    "bytearray": (bytearray(b"abc"), "mutable, binary data"),
    "memoryview": (memoryview(b"abc"), "view over binary data"),
    "NoneType": (None, "represents no value"),
}


for name, (value, info) in examples.items():
    print(f"{name:10} {value!r:20} {info}")


@dataclass
class MyClass:
    instance_variable_int: int
    class_variable_int: ClassVar[int]
