# Do not edit list when iterating over it
# it will not iterate over all elements in the list
my_list = ["A", "B", "C"]
for i in my_list:
    if i == "B":
        my_list.remove("B")
    print(i)

# will not print "C"
print("-----------------")

# If you must edit the list, iterate it backwards
my_list2 = ["A", "B", "C"]
for item in reversed(my_list2):
    if item == "B":
        my_list2.remove("B")
    print(item)
