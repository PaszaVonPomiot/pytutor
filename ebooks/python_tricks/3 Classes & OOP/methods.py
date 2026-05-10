"""
Instance, Class and Static Methods
Using corrent method clearly communicates intent of the method and limits the scope of what method can access or change.

Instance methods
Default method that accepts `self` as first argument. 

`self` points to instance of the class and  allows access to all instance attributes, methods and even parent class (via `self.__class__`).

Instance method can modify instance and class state.

Class methods
Defined with `@classmethod` decorator this method accept `cls` as first argument which points to class instead of instance when the method is called.

Class method can modify class state.

Class methods are good way of creating factory functions.
"""

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

p = Pizza.margherita()
p.ingredients

# Static methods
# Defined with `@staticmethod` decorator this method doesn't accept `self` or `cls` arguments. It is independent of any class or instance variables. It works like a regular function within class namespace.
#
# Static method cannot modify class or instance state.

# Module methods
# Functions outside the class.
