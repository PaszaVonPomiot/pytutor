from itertools import repeat
from timeit import timeit


def loop_using_repeat():
    for _ in repeat(None, 10_000_000):
        ...


def loop_using_range():
    for _ in range(10_000_000):
        ...


repeat_time = timeit(loop_using_repeat, number=10)
range_time = timeit(loop_using_range, number=10)

print(f"Time using repeat: {repeat_time} seconds")
print(f"Time using range: {range_time} seconds")
