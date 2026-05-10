"""
lambda arguments: expression
"""

# single argument
double = lambda x: x * 2  # lambda should not be assigned
print(double(3))

print((lambda x: x * 2)(3))

# multiple arguments
print((lambda x, y: (x + y) / 2)(24, 6))

# lambda with higher order function - map
squared_input_numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, squared_input_numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]


# lambda with higher order function - filter
filtered_input_numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, filtered_input_numbers))
print(even_numbers)  # Output: [2, 4]
print("odd numbers:", list(filter(lambda x: x % 2, filtered_input_numbers)))


# lambda with higher order function - max
mylist = [(3, 4), (1, 7), (5, 23)]
print(max(mylist, key=lambda x: x[1]))
