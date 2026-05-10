for ascending_index in range(10):  # Exclusive of 10
    print(ascending_index)

for signed_index in range(-10, 10):  # Exclusive of upper bound, inclusive of lower bound
    print(signed_index)

for stepped_index in range(
    -10, 10, 20
):  # Exclusive of upper bound, inclusive of lower bound, step of 2
    print(stepped_index)

basic_range = range(10)

print(type(basic_range))  # range(0, 10)

from collections.abc import Sequence

print(issubclass(range, Sequence))  # Pylance even complains about this, but it's true

sequence_range = range(10)

print(f"Fetching the first element: {sequence_range[0]}")
print(f"Fetching the last element: {sequence_range[-1]}")
print(f"Fetching the second element: {sequence_range[1]}")
print(f"Length of the range: {len(sequence_range)}")
print(f"Index of 5: {sequence_range.index(5)}")
print(f"Count of 5: {sequence_range.count(5)}")
print(f"Slice of the range: {sequence_range[2:5]}")  # This returns a range object
print(f"Slice of the range: {sequence_range[2:5:2]}")  # This returns a range object
print(f"Reversed range: {list(reversed(sequence_range))}")
print(f"min of the range: {min(sequence_range)}")
print(f"max of the range: {max(sequence_range)}")

from sys import getsizeof

memory_range = range(0, 20, 2)
my_list = list(memory_range)

print(getsizeof(memory_range))
print(getsizeof(my_list))

descending_range = range(10, 0, -2)
print(list(descending_range))

empty_descending_range = range(10, 20, -2)
print(list(empty_descending_range))
