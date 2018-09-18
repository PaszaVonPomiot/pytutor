def check_if_ingroup(number, group):
    if number in group:
        return True
    return False


print(check_if_ingroup(2, [2, 4, 6, 4, 7, 8, 9, 0, 11]))
