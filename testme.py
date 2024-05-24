#!/bin/python3
import numpy as np
import time
from typing import *
from array import array

def speedTest(f: np.ndarray | list):
    pass
# NumPy array operation
array_size = 1000000
np_array = np.arange(array_size)
start_time = time.time()
np_result = np_array * 2
print("NumPy array operation took ", time.time() - start_time)

# Python list operation
py_list = list(range(array_size))
start_time = time.time()
py_result = [x * 2 for x in py_list]
print("Python list operation took ", time.time() - start_time)

# Python list operation
py_array = array("i",range(array_size))
start_time = time.time()
py_result = [x * 2 for x in py_array]
print("Python array operation took", time.time() - start_time)
