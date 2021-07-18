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
Single Underscore: _
"""
