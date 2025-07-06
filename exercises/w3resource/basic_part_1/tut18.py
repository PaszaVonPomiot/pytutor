lista = []

while True:
    try:
        lista.append(int(input()))
    except ValueError:
        break


suma = sum(lista)
if lista.count(lista[0]) == len(lista):
    print(3*suma)
else:
    print(suma)
