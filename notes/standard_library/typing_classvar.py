"""
For class ClassVar is just type annotation that is redundant.
For dataclass ClassVar makes instance variable actual class variable.
"""

from dataclasses import dataclass
from typing import ClassVar


@dataclass
class MyClass:
    instance_variable_int: int
    class_variable_int: ClassVar[int]
