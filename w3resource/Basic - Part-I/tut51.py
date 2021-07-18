import cProfile
def sum():
    print(5*4)
cProfile.run('sum()')