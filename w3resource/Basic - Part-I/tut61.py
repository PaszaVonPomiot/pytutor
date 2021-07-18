def to_inches(feet):
    return feet * 12

def to_yards(feet):
    return feet / 3

def to_miles(feet):
    return  feet / 5280

feet = float(input("feet: "))
print(to_inches(feet))
print(to_yards(feet))
print(to_miles(feet))

