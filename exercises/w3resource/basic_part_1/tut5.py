name_surname = str(input("Name and surname: ")).split(" ")

for i in reversed(name_surname):
    print(i, end=" ")
