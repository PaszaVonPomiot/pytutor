"""
A tail call is a function call that happens as the last action in a function.
The result of the function call is immediately returned without further computation.
Although Python does not do TCO (Tail Call Optimization) to prevent stack overflow,
it does some optimizations.
"""

# Tail call


def another_function(n: int) -> int:
    return 2 * n


def tail_call(n: int) -> int:
    return another_function(n)  # Tail call: it's the last thing done


def not_tail_call(n: int) -> int:
    return 1 + another_function(n)  # Not a tail call: still does +1 after the call


# Tail recursion - when the same function is called
def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n - 1) * n


def tail_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_factorial(n - 1, accumulator * n)
