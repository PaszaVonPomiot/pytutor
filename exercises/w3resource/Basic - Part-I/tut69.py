integers = [9, 12, 6]

middle_value = sum(integers) - max(integers) - min(integers)
sorted_integers = [min(integers), middle_value, max(integers)]
print(sorted_integers)


sorted_integers2 = sorted(integers)
print(sorted_integers2)
