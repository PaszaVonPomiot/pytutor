from typing import (
    Any,
    Callable,
    ClassVar,
    Generic,
    Iterable,
    Mapping,
    Sequence,
    TypeVar,
)

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


# type annotation with built-in types
def funk(a: int, b: float, c: list, d: dict, e: tuple, f: str, g: bool) -> None:
    print(a, b, c, d, e, f, g)


# print function annotations
print(funk.__annotations__)


x: list[str] = []  # accepts empty list, but str itself cannot be None
y: str | None = None
z: list[str | int] = ["a", 2]

Sequence[int | str]  # eg. list, tuple, str; ordered collection
Iterable[int | str]  # eg. list, tuple, set, dict, str, generator
Mapping[str, int]  # eg. dict


# typing examples
names: list[str] = ["Guido", "Jukka", "Ivan"]
version: tuple[int, ...] = (3, 7, 1)  # variable length tuple
versions2: tuple[int, int, str]  # fixed length tuple
options: dict[str, bool] = {"centered": False, "capitalize": True}


# Variable type - used e.g. to have relationship between argument type and return type
def first(a: list[str | int]) -> str | int:  # room for error
    return a[0]


print(first([1, "2"]))


# Variable type with upper bound
T_my = TypeVar("T_my", bound=int)  # allows for int and its subtypes


# Generic types
u: list = [1, "2"]  # this is generic type of list[Any]
w: dict = {"ass": 4}  # this is generic type of list[Any, Any]
c: Callable = sum

# Custom generic types
# Type of contents is set when we instantiate the class. Then the instance will only accept that type.

G = TypeVar("G")


class Stack(Generic[G]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: list[G] = []

    def push(self, item: G) -> None:
        self.items.append(item)

    def pop(self) -> G:
        return self.items.pop()


stack = Stack[int]()
stack.push(2)
stack.pop()
stack.push("x")
