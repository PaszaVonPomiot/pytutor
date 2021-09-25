import sys

# oszczędność RAM - lazy evaluation
def liczby(max):
    number = 0
    while number < max:
        number += 1
        yield number

generator = liczby(1000000)
lista = list(liczby(1000000))

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

# łatwiejszy/czytelniejszy sposób na tworzenie iteratorów