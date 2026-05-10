class Base:
    def __init__(self, a=2, b=5) -> None:
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

class Inheritance(Base):
    def __init__(self, a, b) -> None:
        super().__init__(a=a, b=b)
    pass

class Composition:
    def __init__(self) -> None:
       self.base = Base()
