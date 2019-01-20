#!/usr/bin/env python3

import multiprocessing
import time
import random



    

processes = []
p1 = multiprocessing.Process(target=random_number)
processes.append(p1)

if __name__ == '__main__':
    p1.start()

