import struct

# 5 string characters
print(struct.calcsize("5s"))

# 2 integer values
print(struct.calcsize("2i"))

# 10 boolean values
print(struct.calcsize("10?"))
