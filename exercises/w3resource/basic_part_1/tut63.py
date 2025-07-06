from pathlib import Path


sciezka = Path(__file__).absolute()
filename = 'tut12.py'
sciezka2 = Path(filename).absolute()
print(sciezka)
print(sciezka2)