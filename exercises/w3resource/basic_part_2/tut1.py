# https://www.w3resource.com/python-exercises/basic/

numlist =[]
while True:
    try:
        number = int(input("Number: "))
    except:
        break
    numlist.append(number)


if len(numlist) == len(set(numlist)):
    print("Distinct")
else:
    print("Not distinct")
