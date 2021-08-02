"""
str() calls __str__ method in pythonic way
repr() calls __repr__ method in pythonic way

__str__ is string conversion dunder method that should be readable
Ideally it should be pretty string representation of an object for users
eg. '2021-08-02'

__repr__ is string conversion dunder method that should be unambiguous
Ideally it should be complete string representation of an object so that eval() can create it.
It should be useful for developers.
eg. 'datetime.date(2021, 8, 2)'
"""

import datetime

today = datetime.date.today()
str(today)  # '2021-08-02'
repr(today)  # 'datetime.date(2021, 8, 2)'

"""
Always add a __repr__ to your classes. 
The default implementation for __str__ just calls __repr__ 
"""


class Car:
    def __init__(self, color) -> None:
        self.color = color

    def __str__(self) -> str:
        return f"__str__ {self.color}"

    def __repr__(self) -> str:
        return f"__repr__ {self.color}"


car = Car("red")

# repr conversion
car
repr(car)
f"{car!r}"
[car]
(car,)
{car: 1}

# str conversion
str(car)
print(car)
f"{car!s}"


"""
Use conversion flag to explicitly call str or repr conversions
"""
f"{car!s}"
f"{car!r}"


"""
The default __repr__ implementation is useless
"""


class Animal:
    pass


animal = Animal()

str(animal)
