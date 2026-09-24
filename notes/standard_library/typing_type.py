"""
Create new type alias (modern way)
"""

type MyType = list[tuple[int, int, int]]
points: MyType = [(1, 2, 3), (4, 5, 6), (7, 8, 1)]


def average(nums: list[int] | tuple[int]) -> float:
    """Calculate the average of a list of numbers."""
    return sum(nums) / len(nums)


average([1, 2, 5])
