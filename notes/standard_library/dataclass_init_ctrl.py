"""
In order to make dataclass field unparametrized exclude it from init.
"""

from dataclasses import dataclass, field


class Counter1:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


@dataclass
class Counter2:
    count: int = field(default=0, init=False)  # count cannot be passed as argument

    def increment(self):
        self.count += 1


Counter1(count=1)  # error
Counter2(count=2)  # error
