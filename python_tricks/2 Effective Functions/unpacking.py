"""
Function Argument Unpacking

* in function call it upacks iterables (lists, tuples, generator expressions, dictionary keys)
into positional arguments
"""
tuple_vec = 2, 5, 7
print(*tuple_vec)

genexpr = (x * x for x in range(5))
print(*genexpr)


"""
** in function call unpacks dictionaries into keyword arguments
"""
