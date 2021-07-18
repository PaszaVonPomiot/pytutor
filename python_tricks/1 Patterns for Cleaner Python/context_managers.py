"""
Context Managers and the with Statement

The with statement simplifies exception handling by encapsu-
lating standard uses of try/finally statements in so-called
context managers.
Most commonly it is used to manage the safe acquisition and
release of system resources. Resources are acquired by the
with statement and released automatically when execution
leaves the with context.
Using with effectively can help you avoid resource leaks and
make your code easier to read.

Useful for connecting to database, opening file, API, etc.


"""

# Class context manager via __enter__ and __exit__ methods
class ContextManagerEnabledClass:
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        return self.text

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.text:
            self.text = "exit"
            print(self.text)


string = ContextManagerEnabledClass("enter")

with string as s:
    print(s)

# Second example of class-based context manager
class ContextManager:
    def __init__(self):
        print("init method called")

    def __enter__(self):
        print("enter method called")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("exit method called")


with ContextManager() as manager:
    print("with statement block")

########################################
# Function context manager
from contextlib import contextmanager


@contextmanager
def ContextManagerFunction():
    # Before yield as the enter method
    print("Enter method called")
    yield
    # After yield as the exit method
    print("Exit method called")


with ContextManagerFunction() as manager:
    print("with statement block")
