# Iterator protocol

iterable = [
    1,
    2,
    3,
    4,
    5,
]  # skończona, już wygenerowana iterowalna lista (również tuple, dict, file, str)
# iterable posiada metodę __iter__()

# stwórz iterator
[].__iter__()
iter([])


# stworzenie iteratora dla obiektu iterowalnego; predefiniowany iterator listy
iterator = iter(
    iterable
)  # iterator - obiekt, który zwraca kolejno po jednym elemencie z obiektu iterowalnego; pamięta swoją pozycję
# iterator posiada metodę __next__()

# iteruj
iterator.__next__()
next(iterator)


# jawne użycie iteratora za pomocą funkcji next() - czyli iteracja
print(next(iterator))  # zwróć kolejny element z kontenera
print(next(iterator))  # przy braku kolejnego elementu - StopIteration
print(next(iterator))


# niejawne użycie iteratora tylko na czas trwania pętli
for liczba in [1, 2, 3, 4, 5]:
    pass
