"""
Custom slice object can be created using slice() function.
It's useful when reusing slice logic in multiple places.
"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_slice = slice(2, 7, 2)

print(my_list[my_slice])  # [3, 5, 7]
print(my_list[2:7:2])  # [3, 5, 7]


my_slice_2 = slice(10, 2, -1)
print(my_list[my_slice_2])

# --------------------------------------------------


# Using slice with subscriptable objects
class MyList:
    def __init__(self):
        self.data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def __getitem__(self, key):
        print(key)
        return self.data[key]


my_list_2 = MyList()
print(my_list_2[1:5])
