"""
Class vs Instance Variable Pitfalls

__Class variables__
are declared inside the class definition (but outside of any instance methods).
They’re not tied to any particular instance of a class. Instead, class variables store their contents on the class itself,and all objects created from a particular class share access to the same set of class variables.

__Instance variables__
are always tied to a particular object instance. 
Their contents are not stored on the class, but on each individual object created from the class.
Therefore, the contents of an instance variable are completely independent from one object instance to the next. And so,modifying an instance variable only affects one object instance at a time.
"""

class Cat:
    class_variable = 0

    def __init__(self, instance_variable) -> None:
        self.instance_variable = instance_variable

print("creating cat instance from class")
cat = Cat(3)
print("cat.instance_variable", cat.instance_variable)
print("cat.class_variable", cat.class_variable)
print("cat.__class__.class_variable", cat.__class__.class_variable)
print()

print("modifying class_variable on class namespace")
Cat.class_variable = 1

print("cat.instance_variable", cat.instance_variable)
print("cat.class_variable", cat.class_variable)
print("cat.__class__.class_variable", cat.__class__.class_variable)
print()

print("overriding class_variable on instance namespace")
cat.class_variable = 2

print("cat.instance_variable", cat.instance_variable)
print("cat.class_variable", cat.class_variable)
print("cat.__class__.class_variable", cat.__class__.class_variable)

# Example of updating class variable on class namespace. Counting number of instances created from the class.

class CountedObject:
    num_instances = 0
    def __init__(self):
        self.__class__.num_instances += 1

a = CountedObject()
b = CountedObject()
c = CountedObject()

print(CountedObject.num_instances)
