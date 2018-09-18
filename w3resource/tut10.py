
def nnn():
    n = int(input("enter integer: "))
    a = int("%s" % n)
    b = int("%s%s" % (n, n))
    c = int("%s%s%s" % (n, n, n))
    eval = a + b + c
    return eval
    
print(nnn())
