# any triplet that sums to zero
# SLOW SOLUTION
from itertools import permutations

nums = [1, -6, 4, 2, -1, 2, 0, -2, 5, 3, ]
perm = set("".join(x) for x in permutations("0000000111"))
win_combinations = []

for combination in perm:
    summed = 0
    for i, binary in enumerate(combination):
        if int(binary):
            summed += nums[i]
    print("wynik:", combination, summed)
    if summed == 0:
        win_combinations.append(combination)

print("win_combinations: ", win_combinations)

for win_combination in win_combinations:
    win_values = []
    for i, binary in enumerate(win_combination):
        if int(binary):
            win_values.append(nums[i])
    print(win_values)



# neighbor triplets that sum to zero
# TODO