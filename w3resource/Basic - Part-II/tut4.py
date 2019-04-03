# any triplet that sums to zero
from random import randint
from itertools import permutations

nums = [randint(-15,15) for x in range(20)]
print(nums)


index_list = [x for x in range(len(nums))]
perms = set(x for x in permutations(index_list, 3))

for perm in perms:
    selected_nums = [nums[x] for x in perm]
    if not sum(selected_nums):
        print(selected_nums, sum(selected_nums))

# # neighbor triplets that sum to zero
# # TODO