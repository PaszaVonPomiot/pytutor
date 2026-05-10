def print_lcm(a_base, b_base):
    current_a = a_base
    current_b = b_base

    while True:
        print(current_a, current_b, sep=" ")
        if current_a == current_b:
            print("NWW: %i" % current_a)
            break
        elif current_a > current_b:
            current_b += b_base
        elif current_a < current_b:
            current_a += a_base

print_lcm(7, 9)
    
