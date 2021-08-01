"""
Decorator is a callable that takes a callable as input and returns another callable
Callable - eg. function, class, method
"""

"""
using decorator explicitly - decorates callable call
you need to use decorator for each function call
"""


def null_decorator(func):
    return func


def greet():
    return "Hello!"


null_decorator(greet())

"""
using @ syntax - decorates callable definition
causes function to be decorated without modifying original function; original is not available
"""


@null_decorator
def greet():
    return "Hello!"


greet()

"""
Actual decorator function
Returns wrapper function which is a closure (inner function that has access to outer function argument, after outer function has ended)
Closure uses func from argument and modifies its result
"""


def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper  # returns function


@uppercase
def greet():
    return "Hello!"


greet()

"""
Decorator stacking - applied from bottom to the top
"""


@decor2
@decor1
def greet():
    return "Hello!"


# Is equivalent to
decor2(decor1(greet))

"""
Decorating Functions That Accept Arguments
"""


def proxy(func):
    def wrapper(*args, **kwargs):  # COLLECTS positional and keyword arguments from func
        result = func(*args, **kwargs)
        result.append("trzy")
        return result  # UNPACKING - forwards arguments to original function

    return wrapper


@proxy
def licz(word1, word2):
    return [word1, word2]


licz("raz", "dwa")
