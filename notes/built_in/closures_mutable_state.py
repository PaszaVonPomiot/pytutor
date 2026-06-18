from typing import Callable


# Use case: Closure with mutable state
def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        nonlocal count  # allows us to modify the count variable from the outer scope
        count += 1
        return count

    return increment


counter_a = counter()
print(counter_a())  # Output: 1
print(counter_a())  # Output: 2
