from typing import Callable


# Use case: Function factory with closure
def tax_calculator(tax_rate: float) -> Callable[[float], float]:

    def get_tax_amount(money: float) -> float:
        return money * tax_rate  # tax_rate will stay when outer function returns

    return get_tax_amount


get_low_taxes = tax_calculator(tax_rate=0.07)
get_high_taxes = tax_calculator(tax_rate=0.23)

print(get_low_taxes(1000))  # Output: 70.0
print(get_high_taxes(1000))  # Output: 230.0
