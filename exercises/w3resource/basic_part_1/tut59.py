def inches_to_cm(inches):
    return inches * 2.54

def feet_to_cm(feet):
    return feet * 30.48

feet = float(input("feet: "))
feet_cm = feet_to_cm(feet)
print(feet_cm, "cm")

inches = float(input("inches: "))
inches_cm = inches_to_cm(inches)
print(inches_cm, "cm")
