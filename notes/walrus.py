# walrus operator allows to both assign a value to a variable and return that value as part of an expression
# variable := expression

# expression is part of code that produces a value:
"thing"

1 < 3
5 * 5
len("hello")
0 and 2

# Example 1 - while loop
line = input("Enter text: ")
while line != "exit":
    print(f"You entered: {line}")
    line = input("Enter text: ")

while (line := input("Enter text: ")) != "exit":
    print(f"You entered: {line}")


# Example 2 - list comprehension
results = []
for num in range(10):
    squared = num * num
    if squared > 20:
        results.append(squared)

results = [squared for num in range(10) if (squared := num * num) > 20]


# Example 3 - conditional
my_list = [1, 2, 3, 4, 5, 6]

n = len(my_list)
if n > 5:
    print(f"List has more than 5 elements; it has {n} elements.")

if (n := len(my_list)) > 5:
    print(f"List has more than 5 elements; it has {n} elements.")
