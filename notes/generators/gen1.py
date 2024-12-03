# wygeneruj ciąg liczb naturalnych do nieskończoności po jednej

def fun():
    global a
    a += 1
    return a

a = 0  # potrzebna extra zmienna; odseparowana od funkcji

print(fun())
print(fun())
print(fun())
print(fun())
print(fun())
