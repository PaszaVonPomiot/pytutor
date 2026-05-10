"""
Defining Your Own Exception Classes

Define exception with descriptive name based on generic `Exception` or more specific `ValueError` or `TypeError`
"""

class SimpleNameTooShortError(ValueError):
    pass

def validate_min_length(name):
    if len(name) < 10:
        # name in the constructor
        raise SimpleNameTooShortError(name)

validate_min_length('Nikita')

# For own module you can create hierarchy of exceptions so that you can catch whole category of concrete exceptions

class BaseValidationError(ValueError):
    pass

class NameTooShortValidationError(BaseValidationError):
    pass
class NameTooLongValidationError(BaseValidationError):
    pass

def validate_length(name):
    if len(name) < 5:
        # name in the constructor
        raise NameTooShortValidationError(name)
    elif len(name) > 10:
        raise NameTooLongValidationError(name)

try:
    validate_length('1234')
except BaseValidationError as err:
    print(err)
