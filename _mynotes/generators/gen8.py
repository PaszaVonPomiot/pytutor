def check_prime(number):
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def primes(max):  # z parametrem
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number


g = primes(100000)

# for przyjmuje obiekt iterowalny o nieoznaczonej liczbie elementów
for liczba in g:  
    print(next(g))


# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break