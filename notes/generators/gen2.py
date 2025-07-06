class A:
    def __init__(self):
        self.i = 0

    def daj(self):
        self.i += 1
        return self.i


a = A()

print(a.daj())
print(a.daj())
print(a.daj())
print(a.daj())
print(a.daj())
