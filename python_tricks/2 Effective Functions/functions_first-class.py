def yell(text):
    return text.upper() + "!"


"""
Functions Are Objects

A variable pointing to a function
and the function itself are really two separate concerns.
"""
bark = yell
del yell
bark("woof")  # still works
bark.__name__  # name of the function


"""
Functions Can Be Stored in Data Structures
"""
funcs = [bark, str.lower, str.capitalize]


"""
Functions Can Be Passed to Other Functions
Functions that can accept other functions as arguments are called higher-order functions
"""


def greet(func):
    greeting = func("Hi, I am a Python program")
    print(greeting)


greet(bark)

# map(function, iterable) is higher-order function
list(map(bark, ["hello", "hey", "hi"]))

"""
Functions Can Be Nested
These are often called nested functions or inner functions
Inner functions are not accessible from outside the function but you can return them
"""


def speak(volume):
    def whisper(text):
        return text.lower()

    def shout(text):
        return text.upper()

    if volume < 5:
        return whisper
    else:
        return shout


speak(4)("ahaaaa")
speak(6)("ahaaaa")


"""
Functions Can Capture Local State
Closure is a nested function which has access to a free variable from an enclosing function that has finished its execution. 
A free variable is a variable that is not bound in the local scope.
"""


def make_adder(n):
    def add(x):
        return x + n

    return add


fu = make_adder(2)  # fu still has access to n even after parent function has ended
fu(3)

# second example


def get_speak_func(volume, text):
    # Inner function without argument captures and returns parent function argument
    def whisper():
        return (
            text.lower() + "..."
        )  # has access to free variable after parent function has finished its execution

    def yell():
        return text.upper() + "!"

    if volume > 0.5:
        return yell
    else:
        return whisper


get_speak_func(3, "ahaaaaaa")()


"""
Objects Can Behave Like Functions by defining __call__ method
"""


class SimpleClass:
    pass


callable(SimpleClass)  # is class callable
callable(SimpleClass())  # is instance callable


class SimpleClass:
    def __call__(self):
        print("Im a function")


callable(SimpleClass)  # is class callable
callable(SimpleClass())  # is instance callable

# to check if callable
callable(1)
callable(1.2)
callable("text")
callable([])
callable(object)
