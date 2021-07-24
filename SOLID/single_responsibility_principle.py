class Jeden:
    @staticmethod
    def print():
        print("text")


class Dwa(Jeden):
    @staticmethod
    def print():
        print("dupa")


Dwa().print()
