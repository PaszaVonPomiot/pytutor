"""
Single Leading Underscore: _var
Convention for private object; will not be imported by wildcard import unless specified in __all__
"""
pass

"""
Single Trailing Underscore: var_
Convention to avoind naming conflicts
"""
pass

"""
Double Leading Underscore: __var
Python does name mangling which prevents overriding this variable by a subclass
"""


class Test:
    def __init__(self):
        self.__abc = 123


class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.__abc = 456


t = Test()
print(dir(t))  # '_Test__abc'


"""
Double Leading and Trailing Underscore: __var__
Dunder methods or magic methods - have special use in language like __init__ or __call__
Not affected by name mangling.
"""

"""
Single Underscore: _
“don’t care” variable that is never used. Eg. in "for _ in iterable" loop

ALSO ONLY IN INTERPRETER REPL SESSION
>>> _=5
>>> print(_)
5
>>> 3+7
10
>>> print(_)
5
"""
# unpacking tuple but interested only in mileage
car = ("red", "auto", 12, 3812.4)
_, _, _, mileage = car
