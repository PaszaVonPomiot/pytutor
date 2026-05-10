"""
dict instead of multiple if/else
"""

def conditional_one():
    return 1

def conditional_two():
    return 2

def conditional_three():
    return 3

conditional_choice = 1

if conditional_choice == 1:
    conditional_one()
elif conditional_choice == 2:
    conditional_two()
else:
    conditional_three()

def action_one():
    return 1

def action_two():
    return 2

def action_three():
    return 3

action_choice = 1

actions = {
    1: action_one,
    2: action_two,
}

action = actions.get(action_choice, action_three)
action()
