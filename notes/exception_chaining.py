"""
Exception Chaining is allowing you to raise a new exception while preserving the context of the original exception.
Implicit Exception Chaining in Python puts the original exception in `__context__` attribute of the new exception.
To remove the original exception from the context, use `raise ... from None`.
"""


# Remove the original exception from the context
def parse_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Expected an integer, got: {value!r}") from None


parse_int("abc")
