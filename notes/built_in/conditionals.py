# you can replace many conditional statements with a dictionary


def a():
    print("a")


def b():
    print("b")


def c():
    print("c")


def default():
    print("default")


option = "b"
choices = {"a": a, "b": b, "c": c}
choice = choices.get(option, default)
choice()
