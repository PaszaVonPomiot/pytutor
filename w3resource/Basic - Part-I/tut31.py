from datetime import datetime
start_time = datetime.now()

########

def najwspmian(a, b):
    for dz in range(min(a, b), 0, -1):
        if a % dz == 0 and b % dz == 0:
            nwd = dz
            print(nwd)
            break


najwspmian(6726, 3465)

########


end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))