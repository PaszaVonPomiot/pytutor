def inches_to_cm(inches):
    return inches * 2.54

def feet_to_cm(feet):
    return feet * 30.48

feet = float(input("feet: "))
cm = feet_to_cm(feet)
print(cm, "cm")

inches = float(input("inches: "))
cm = inches_to_cm(inches)
print(cm, "cm")

