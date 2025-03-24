import numpy as np
from fontTools.cffLib import topDictOperators
from numpy import random
import seaborn as sns
from matplotlib import pyplot as plt

# vectorization

list1 = [2,3,4,5]
list2 = [2,7,8,9]
list3 = []

# for i in range(len(list1)):
#     list3.append(list1[i]+list2[i])

# for i,j in zip(list1, list2):
#     list3.append(i+j)

# print(list3)

# vectorization using numpy

# list4 = np.add(list1,list2)
# print(list4)

# vectorization using own function

# def add(x,y):
#     return x+y
#
# add = np.frompyfunc(add, 2, 1)
# print(add(list1,list2))

# Creating calculator using numpy array

test_1 = np.array([12,15,16,20,60])
test_2 = np.array([6,7,9,10,15])

# print(f"test_1 + test_2 = {np.add(test_1, test_2)}")
# print(f"test_1 - test_2 = {np.subtract(test_1, test_2)}")
# print(f"test_1 * test_2 = {np.multiply(test_1, test_2)}")
# print(f"test_1 / test_2 = {np.divide(test_1, test_2)}")
# print(f"test_1 % test_2 = {np.mod(test_1, test_2)}")
# print(f"test_1 ** test_2 = {np.power(test_1, test_2)}")
# print(f"Absolute Value : test_1 / test_2 = {np.absolute(test_1, test_2)}")
# print(f"DivMod : test_1 / test_2 = {np.divmod(test_1, test_2)}")

# Rounding in Numpy

arr = np.array([0.5, 0.51, 0.49, 1.0001, 2.3456, 3.4567, 4.5678, 5.6789])
# print(np.trunc(arr))
# print(np.fix(arr))
# print(np.floor(arr))
# print(np.ceil(arr))
# print(np.around(arr))

