a = a_base = 7
b = b_base = 9

while True:
    print(a, b, sep=" ")
    if a == b:
        print("NWW: %i" % a)
        break
    elif a > b:
        b += b_base
    elif a < b:
        a += a_base
    
