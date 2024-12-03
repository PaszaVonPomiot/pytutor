# generator - iterator i iterable stworzony z funkcji z yield
def gen_fun():  # funkcja generatorowa
    i = 0
    while True:
        i += 1
        yield i


g = gen_fun()  # wywołanie funkcji generatorowej tworzy generator

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

