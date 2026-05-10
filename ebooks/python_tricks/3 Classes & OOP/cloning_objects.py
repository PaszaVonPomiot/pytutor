"""
Cloning objects

Assignment statements in Python do not create copies of objects, they only bind names to an object.

Shallow copy
Shallow copy creates new object and populates it with references to child objects of original. Only collection object is a new object.

In order to shallow copy mutable Python collections you can call their factory functions on existing collections.

Shallow copied list is not fully independent.
"""

shallow_source_list = [1, 2 , [3]]
original_dict = {"a": 1, "b": 2, "c": 3}
original_set = {1, 2, 3}

shallow_copied_list = list(shallow_source_list)
new_dict = dict(original_dict)
new_set = set(original_set)

nested_source_list = [1, 2 , [3]]  # nested element
nested_copied_list = list(nested_source_list)

nested_source_list[0] = "X"
nested_source_list[2][0] = "Y"

print(nested_source_list)
print(nested_copied_list)

# Deep copy
# Deep copy creates a new collection object and then recursively populates it with copies of the child objects found in the original. Both collection object and its recursive content are new objects.
#
# Deep copied list is fully independent.

import copy
deepcopy_source_list = [1, 2 , [3]]
deep_copied_list = copy.deepcopy(deepcopy_source_list)

deepcopy_source_list[0] = "X"
deepcopy_source_list[2][0] = "Y"

print(deepcopy_source_list)
print(deep_copied_list)

# You can copy arbitrary objects like classes using shallow or deep copy from `copy` module
