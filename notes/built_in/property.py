"""
A Python property is a descriptor that lets you access methods like simple attributes.
It allows you to add logic (validation, computation) when getting, setting, or deleting values.

Created with @property decorator or property() function.
Uses the descriptor protocol under the hood.

Using a property communicates that something is state-like, cheap to access, safe to read often.
"""


# Managed attribute with decorator
class DecoratedPropertyExample:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


dpe = DecoratedPropertyExample()
dpe.x


# Managed attribute without decorator
class ManualPropertyExample:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
