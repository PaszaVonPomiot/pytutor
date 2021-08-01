"""
* and ** in definition means packing
* and ** in function call means unpacking
"""


def foo(required, *args, **kwargs):
    print(required)
    if args:  # tuple
        print(args)
    if kwargs:  # dict
        print(kwargs)


"""
packed arguments can be changed before passing them along
"""


def foo(x, *args, **kwargs):
    kwargs["name"] = "Alice"
    new_args = args + ("extra",)
    bar(x, *new_args, **kwargs)


"""
Eg. extending parent class __init__
"""


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage


class AlwaysBlueCar(Car):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # simply pass args
        self.color = "blue"  # override color attribute
