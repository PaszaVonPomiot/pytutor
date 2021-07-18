def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))
    print("Name: %s\nAge: %d\nAddress: %s" % (name, age, address))

personal_details()