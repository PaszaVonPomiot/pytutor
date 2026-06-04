"""
Borg Pattern - all instances share the same state.

The Borg pattern is an alternative to the Singleton pattern that allows multiple
instances to exist, but ensures they all share the same state. Instead of
restricting the number of instances, the Borg pattern makes all instances
reference the same underlying data store by setting each instance's `__dict__`
to point to a shared class-level dictionary.

This means:
- Multiple instances can be created and are distinct objects (`a is not b`).
- All instances access and modify the same shared state.
- Changes made through one instance are visible to all other instances.

The Borg pattern is useful when you need all instances to behave as if they
were the same object, but still want the flexibility of having multiple
instance references.
"""


class Borg:
    _state = {}

    def __init__(self):
        self.__dict__ = self._state  # instance __dict__ references class _state


a = Borg()
b = Borg()

a.value = 123

print(b.value)  # 123
print(a is b)  # False
