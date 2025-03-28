import math
from math import *
import numpy as np
from numpy import *
import seaborn as sns
from matplotlib import pyplot as plt

# Set operations

arr = np.array([8,2,5,1,6,8])
arr2 = np.array([7,1,6,5,4,1])

new_arr = np.unique(arr)
uni_arr = np.union1d(arr,arr2)
int_arr = np.intersect1d(arr,arr2, assume_unique=True)
diff_arr = np.setdiff1d(arr,arr2, assume_unique=True)
sym_diff_arr = np.setxor1d(arr,arr2, assume_unique=True)

# Hyperbolic

# pi = 180, trigonometry value from the pie
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# print(np.arcsinh(arr)) # same goes for cos, tan

