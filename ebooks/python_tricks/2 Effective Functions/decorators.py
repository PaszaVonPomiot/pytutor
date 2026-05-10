"""
Decorators

Decorator is a callable that takes a callable as input and returns another callable
Callable - eg. function, class, method

using decorator explicitly - decorates callable call
you need to use decorator for each function call
"""

def null_decorator(func):
    return func

def greet_plain():
    return "Hello!"

null_decorator(greet_plain())

# using @ syntax - decorates callable definition
# causes function to be decorated without modifying original function; original is not available

@null_decorator
def greet_with_null_decorator():
    return "Hello!"

greet_with_null_decorator()

# Actual decorator function
# Returns wrapper function which is a closure (inner function that has access to outer function argument, after outer function has ended)
# Closure uses func from argument and modifies its result

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result

    return wrapper  # returns function

@uppercase
def greet_uppercase():
    return "Hello!"

greet_uppercase()

# Decorator stacking - applied from bottom to the top

@decor2
@decor1
def greet_stacked():
    return "Hello!"

# Is equivalent to
decor2(decor1(greet_stacked))

# Decorating Functions That Accept Arguments

def append_word_proxy(func):
    def wrapper(*args, **kwargs):  # COLLECTS positional and keyword arguments from func
        result = func(*args, **kwargs)
        result.append("trzy")
        return result  # UNPACKING - forwards arguments to original function

    return wrapper

@append_word_proxy
def licz(word1, word2):
    return [word1, word2]

licz("raz", "dwa")

# Decorators replace one function with another thus remove some metadata like original docstring
# To solve this always copy metadata from original function using functools.wraps
# This helps debugging

def append_word_proxy_with_metadata(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # COLLECTS positional and keyword arguments from func
        result = func(*args, **kwargs)
        result.append("trzy")
        return result  # UNPACKING - forwards arguments to original function

    return wrapper

# Topics not covered:
# - Decorator that accepts argments
# - Decorator as a class
