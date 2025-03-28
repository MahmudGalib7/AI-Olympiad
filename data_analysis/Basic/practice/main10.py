from math import log
import numpy as np
from numpy import *
import seaborn as sns
from matplotlib import pyplot as plt

list1 = [10,15,25,5]
list2 = [2,5,1,6,8]

# sum
# print(np.sum([list1, list2], axis=1))

# cumulative sum
# print(np.cumsum([list1, list2]))

# logarithm

log_arr = np.arange(1,10)
# print(np.log2(log_arr))
# print(np.log10(log_arr))
# print(np.log(log_arr))

# def scaler_log(x, base):
#     if isinstance(x,np.ndarray) or isinstance (base,np.ndarray):
#         raise TypeError("")
#
#     return log(x, base)
#
#
# np_log =np.frompyfunc(scaler_log,2,1)
# print(np_log(100,15))

# product
# print(np.prod([list1, list2]))
# print(np.cumprod([list1, list2]))

# difference
# print(np.diff(list1))
# print(np.diff(list1, 2))

# lcd, gcd
# num1 = 4
# num2 = 12
#
# print(f"LCM : {np.lcm(num1, num2)}")
# print(f"GCD : {np.gcd(num1, num2)}")
#
# test_arr = [1,2,3,4,5]
# print(np.lcm.reduce(test_arr))
# print(np.gcd.reduce(test_arr))

# Trigonometry

# pi = 180, trigonometry values from the pie
# print(np.sin(np.pi / 2))
# arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
# print(np.sin(arr)) # same for cos, tan

# deg -> rad
# arr_deg = np.array([90, 180, 270, 360])
# x = np.deg2rad(arr_deg)
# print(x)

# rad -> deg
# arr_rad = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
# print(np.rad2deg(arr_rad))

# angles values -> rad
# print(np.arcsin(1.0)) # similarly arccos & arctan
# arr = np.array([1, -1, 0.1])
# x = np.arcsin(arr)
# print(x)

# hypo
# base = 5
# perp = 12
# print(np.hypot(base, perp))