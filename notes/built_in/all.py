empty_list: list[str] = []
all(empty_list)  # Checks if there are no False elements in the list
# Since the list is empty, it returns True

mixed_list_with_zero: list[int] = [1, 2, 0, 4, 5]
all(mixed_list_with_zero)  # False because there is a 0 in the list

mixed_list_with_none: list[int | None] = [1, 2, None, 4, 5]
all(mixed_list_with_none)  # None is falsy

class SomeInt:
    def __init__(self, value: int):
        self.value = value

    def __bool__(self):
        return bool(self.value)

objects = [SomeInt(1), SomeInt(2), SomeInt(0)]
all(objects)  # False because SomeInt(0) is falsy

non_empty_string = "hello"
empty_string = ""

print(f"non_empty_string is {all(non_empty_string)}")  # True, all characters are truthy
print(f"empty_string is {all(empty_string)}")  # True, just like empty list

nested_list: list[list[int]] = [[1, 2], [3, 4], []]
all(
    nested_list
)  # the empty list is falsy in this case, since it does not recursively check the nested lists

numbers = (x > 0 for x in range(1, 10))
print(all(numbers))  # all elements are > 0

gen_with_falsy = (x > 0 for x in range(-5, 5))
print(all(gen_with_falsy))  # -5 to -1 are falsy
