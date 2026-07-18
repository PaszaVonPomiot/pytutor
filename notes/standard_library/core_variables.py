"""
Change to one variable does not affect the other variable that was assigned to it.
"""

# Example of changing one variable without affecting the other
a = 1
b = a
a = 2
print(b)  # Output: 1

# Example of swapping two variables - incorrect way
c = 1
d = 2
c = d
d = c
print(c)  # Output: 2
print(d)  # Output: 2

# Example of swapping two variables - correct way
e = 1
f = 2
e, f = f, e
print(e)  # Output: 2
print(f)  # Output: 1
