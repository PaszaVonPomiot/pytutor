from typing import (
    Sequence,
    Iterable,
    Any,
    TypeVar,
    ClassVar,
    Generic,
    TypeAlias,
    Callable,
    NoReturn,
)


# type ...
# type union?
# Generic[]
# TypeVar

# type annotation with built-in types
def funk(a: int, b: float, c: list, d: dict, e: tuple, f: str, g: bool) -> None:
    print(a, b, c, d, e, f, g)


# print function annotations
print(funk.__annotations__)

# list[str] accepts empty list, but str itself cannot be None
x: list[str] = []
y: str | None = None
z: list[str | int] = ["a", 2]

# any sequence annotation (eg. list, tuple, str); union of types
def print_sequ(s: Sequence[int | str]):
    print(s)


def print_iter(i: Iterable[int | str]):
    print(i)


print_sequ([1.1, 2, 3])
print_sequ((1, 2, 3))
print_sequ("123")
print_sequ(True)

# typing examples
names: list[str] = ["Guido", "Jukka", "Ivan"]
version: tuple[int, ...] = (3, 7, 1)  # variable length tuple
versions2: tuple[int, int, str]  # fixed length tuple
options: dict[str, bool] = {"centered": False, "capitalize": True}


# Type alias, old/new notation
T_old_xyz = list[tuple[int, int, int]]
points1: T_old_xyz = [(1, 2, 3), (4, 5, 6), (7, 8, 1)]

T_new_xyz: TypeAlias = list[tuple[int, int, int]]
points2: T_new_xyz = [(1, 2, 3), (4, 5, 6), (7, 8, 1)]

# print module level annotations
# print(__annotations__)

# annotating function that never returns
def stop() -> NoReturn:
    raise Exception("no way")


# Variable type - used e.g. to have relationship between argument type and return type
def first(a: list[str | int]) -> str | int:  # room for error
    return a[0]


print(first([1, "2"]))


T = TypeVar("T")
# or with limited available types
t_strint = TypeVar("t_strint", str, int)

# requires arguments of single type and return value of the same type
def first2(a: list[T]) -> T:
    return int(a[0])


print(first2(["1", "2"]))

# Variable type with upper bound
T_my = TypeVar("T_my", bound=int)  # allows for int and its subtypes

# Variable type

# indicate class variable
class Point:
    xx: int
    yy: int
    points: ClassVar[int] = 0  # indicates that variable should not be used as instance variable

    def __init__(self, xx, points):  # class variable cannot be put as __init__ parameter
        self.xx = xx
        self.points = points


# Callable
cal: Callable[[int, int, int], int]  # [[parameters' types], return type]


def sum_ab(a: int, b: int) -> int:
    return a + b


def double(f: Callable[[int, int], int]) -> int:
    return f(2, 3) * 2


double(sum_ab)

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
