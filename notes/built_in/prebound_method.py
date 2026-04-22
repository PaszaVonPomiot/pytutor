"""
A powerful technique for offering callables at the top level of your
module that share state through a common object.

Useful for sharing state between top-level callables.
"""


class Lamp:
    def __init__(self):
        self.state = False

    def on(self):  # bound method
        self.state = True
        print("ON")

    def off(self):
        self.state = False
        print("OFF")

    def status(self):
        print(self.state)


# Unbound method
Lamp.status  # unbound method - called from class

lamp = Lamp()
Lamp.status(lamp)  # unbound method requires instance argument


# Bound method
Lamp().status()  # instance is bound to the method


# Prebound method (bound method assigned to variable)
status = Lamp().status
status()
