from os import listdir
from os.path import isfile

dir_list = listdir()

# A
for file in dir_list:
    if isfile(file):
        print(file)

print("-----")

# B
[ print(file) for file in dir_list if isfile(file) ]