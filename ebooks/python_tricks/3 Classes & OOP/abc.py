"""
Abstract Base Classes

`abc.ABC` prevents base class from being instantiated directly; needs to be subclassed

`abc.abstractmethod` forces implementation of method before instantiation
"""

from abc import ABC, abstractmethod

# ABC is helper class so that you don't have to use metaclass syntax
class AbstractBase(ABC):
    @abstractmethod
    def foo(self):
        pass
    @abstractmethod
    def bar(self):
        pass

class IncompleteConcrete(AbstractBase):
    def foo(self):
        pass

# TypeError because bar() is not implemented
incomplete_concrete = IncompleteConcrete()

# Standard Base Classes
#
# Will not throw error at the instatiation if method is not implemented. Only at usage.

class StandardBase:
    def foo(self):
        raise NotImplementedError()
    def bar(self):
        raise NotImplementedError()

class StandardConcrete(StandardBase):
    def foo(self):
        return 'foo() called'

standard_concrete = StandardConcrete()
