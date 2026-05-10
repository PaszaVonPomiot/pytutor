"""
walrus operator allows to both assign a value to a variable and return that value as part of an expression
variable := expression
"""

# expression is part of code that produces a value:
"thing"

1 < 3
5 * 5
len("hello")
0 and 2

# Example 1 - while loop
def input_loop_without_walrus():
    input_line = input("Enter text: ")
    while input_line != "exit":
        print(f"You entered: {input_line}")
        input_line = input("Enter text: ")

def input_loop_with_walrus():
    while (walrus_line := input("Enter text: ")) != "exit":
        print(f"You entered: {walrus_line}")


# Example 2 - list comprehension
loop_results = []
for num in range(10):
    squared = num * num
    if squared > 20:
        loop_results.append(squared)

walrus_results = [squared for num in range(10) if (squared := num * num) > 20]


# Example 3 - conditional
my_list = [1, 2, 3, 4, 5, 6]

list_length = len(my_list)
if list_length > 5:
    print(f"List has more than 5 elements; it has {list_length} elements.")

if (walrus_list_length := len(my_list)) > 5:
    print(f"List has more than 5 elements; it has {walrus_list_length} elements.")
