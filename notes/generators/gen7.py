def gen_fun(i=0):  # funkcja generatorowa
    while True:
        i += 1
        yield i
        yield -i


g = gen_fun()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


