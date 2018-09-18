imienazwisko = str(input("podaj imie i nazwisko: ")).split(" ")

for i in reversed(imienazwisko):
    print(i, end=" ")
