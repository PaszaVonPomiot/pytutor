target = [1000, 2000]
range = 100

# test = check > (target - range) and check < (target + range)


def check_if_in_range(liczba, target):
    return abs(target - liczba) < range


liczba = int(input("podaj liczbę: "))

for itarget in target:
    print(check_if_in_range(liczba, itarget))
