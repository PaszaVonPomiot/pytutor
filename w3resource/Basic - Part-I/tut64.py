import os
import time
from datetime import datetime

print(__file__)

creation_time = os.path.getctime(__file__)
modification_time = os.path.getmtime(__file__)
access_time = os.path.getatime(__file__)

print("File creation time: ", datetime.fromtimestamp(creation_time))
print("File modification time: ", datetime.fromtimestamp(modification_time))
print("File access time: ", datetime.fromtimestamp(access_time))
print("-----------------------------------")
print("File creation time: ", time.ctime(creation_time))
print("File modification time: ", time.ctime(modification_time))
print("File access time: ", time.ctime(access_time))
