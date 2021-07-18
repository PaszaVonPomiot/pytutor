from itertools import permutations

string = 'abcd'
perms = [x for x in permutations(string)]

for perm in perms:
    print(''.join(perm))
