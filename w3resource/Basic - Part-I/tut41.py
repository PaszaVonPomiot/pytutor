import os
from pathlib import Path

print(os.getcwd())
print(__file__)
print(os.path.dirname(__file__) + "tut40.py")
print(os.path.isfile("tut40.py"))

print(Path().absolute())
filepath = Path().absolute().joinpath('tut41.py')
print(filepath)
print(os.path.isfile(filepath))


