# dir() function returns a list of names in the current local scope or the specified object.
# It can be used to get the attributes and methods of modules, classes, and instances.
# Result is based on __dir__() method of the object.


class Invoice:
    def __init__(self, amount):
        self.amount = amount


invoice = Invoice(1000)
a = 1

global_namespace = dir()
class_namespace = dir(Invoice)
instance_namespace = dir(invoice)

print("Global Namespace:", global_namespace)
print("Class Namespace:", class_namespace)
print("Instance Namespace:", instance_namespace)
