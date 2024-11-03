number = 39211112


sum_of_digits = sum([int(digit) for digit in str(number)])
print(sum_of_digits)

sum_of_digits2 = sum(map(int, str(number)))
print(sum_of_digits2)
