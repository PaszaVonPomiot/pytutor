from itertools import pairwise

numbers = [1, 2, 3, 4, 5]

for a, b in pairwise(numbers):
    print(a, b)  # 1 2, 2 3, 3 4, 4 5
