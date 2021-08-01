"""
If not explicitly defined, all functions return None
If function doesn't have return value don't write explicit return None unless it helps readability
"""


def foo1(value):
    if value:
        return value
    else:
        return None


def foo2(value):
    """Bare return statement implies `return None`"""
    if value:
        return value
    else:
        return


def foo3(value):
    """Missing return statement implies `return None`"""
    if value:
        return value
