# obiekt, który jednocześnie reaguje na next() i iter()

class Natural:  # stwórzmy własny iterator
    def __init__(self):
        self.i = 0
        
    def __iter__(self):  # potrafi zwrócić iterator
        return self

    def __next__(self):  # jako iterator wiesz co robić przy next()
        self.i += 1
        return self.i


a = iter(Natural())

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))