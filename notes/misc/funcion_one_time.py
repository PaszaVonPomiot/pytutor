"""
Function can use introspection to check if it has been initialized before.
If not, it performs initialization tasks and sets an attribute to indicate that it has been initialized.
Subsequent calls will skip the initialization and only execute the regular code.
"""


# Function that initializes one time
def func_one_time() -> None:
    if not hasattr(func_one_time, "initialized"):
        print("Run once")
        func_one_time.initialized = True
    print("Run every time")


func_one_time()
func_one_time()
