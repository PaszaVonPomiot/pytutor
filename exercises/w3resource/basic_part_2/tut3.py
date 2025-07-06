lista = list(range(30))
print(lista)

for n in lista[2::3]:
    print(n)
    lista.remove(n)  # remove element by value

print(lista)