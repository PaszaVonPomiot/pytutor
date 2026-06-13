def add(a, b):
    """
    >>> add(1,2)
    3

    """
    return a + b


def divide(a, b):
    """
    >>> divide(1, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """
    return a / b


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
