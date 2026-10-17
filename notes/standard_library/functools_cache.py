from functools import cache, lru_cache


# Never-expiring cache
@cache
def get_money(amount: int):
    return amount


# Least Recently Used Cache
@lru_cache(maxsize=3)
def get_money_2(amount: int):
    return amount
