"""
A closure is an inner function that carries state from outer function
after outer function has finished

Create a closure in 3 steps:
1. Define a function inside another function.
2. The inner function refers to variables from the outer function.
3. The outer function returns the inner function.
"""

from typing import Callable


def outer(x: int) -> Callable:
    def inner(y: int) -> int:
        return x + y

    return inner


def tax_calculator(tax_rate: float) -> Callable[[float], float]:

    def get_tax_amount(money: float) -> float:
        return money * tax_rate  # tax_rate will stay when outer function returns

    return get_tax_amount


get_low_taxes = tax_calculator(tax_rate=0.07)
get_high_taxes = tax_calculator(tax_rate=0.23)

print(get_low_taxes(1000))
