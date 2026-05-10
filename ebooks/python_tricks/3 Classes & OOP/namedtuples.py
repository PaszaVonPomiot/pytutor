"""
Namedtuples

Namedtuples work like regular tuples but allow using field names instead of just indices. Use namedtuples to add meaningful fields to tuples but avoid complexity of building a class. Eg. to 2D point could be named tuple with easy equality check without having to implement `__eq__` method in a class. Also accessing attribute is easy like `point.x`

Namedtuple immutable objects are implemented as regular Python classes internally. 

When it comes to memory usage, they are also “better” than regular classes and just as memory efficient as regular tuples.

Create new data type factory function using `namedtuple()` factory function
"""

from collections import namedtuple

# "Car" is typename that will appear in __repr__
CarWithFieldList = namedtuple("CarWithFieldList", ["brand", "mileage", "color"])
field_list_car = CarWithFieldList('tesla', 124556, 'pink')
print(field_list_car)

# Shorthand with iteration

# shorthand
CarWithFieldString = namedtuple("CarWithFieldString", "brand mileage color")
field_string_car = CarWithFieldString('tesla', 124556, 'pink')
print(field_string_car.color)
print(field_string_car[2])

# Packing and unpacking of namedtuple works

CarForUnpacking = namedtuple("CarForUnpacking", "brand mileage color")
unpacked_car = CarForUnpacking('tesla', 124556, 'pink')

default_brand = "fiat"
default_mileage = 1000
default_color = "red"
unpacked_color, unpacked_brand, unpacked_mileage = unpacked_car

print(unpacked_car)
print(*unpacked_car)

# Namedtuples are immutable

ImmutableCar = namedtuple("ImmutableCar", "brand mileage color")
immutable_car = ImmutableCar('tesla', 124556, 'pink')
immutable_car.color = "red"

# To inspect what fields are in namedtuple print `_fields` attribute

InspectableCar = namedtuple("InspectableCar", "brand mileage color")
InspectableCar._fields

# Internally namedtuple is a class therefore it's possible to subclass it. But usually it's not recommended.

SubclassableCar = namedtuple('SubclassableCar', 'color mileage')

class MyCarWithMethods(SubclassableCar):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

# Namedtuple resembles dictionary therefore it's easy to return a dict object with `_asdict()` method.

DictionaryLikeCar = namedtuple("DictionaryLikeCar", "brand mileage color")
dictionary_like_car = DictionaryLikeCar('tesla', 124556, 'pink')
dictionary_like_car._asdict()
