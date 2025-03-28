import numpy as np

# arr = np.array([[1,2,3,4,5], [2,3,4,5,6]])
# print(arr)
# print(arr.shape)

# arr1 = np.array([[1,2,3,4,5], [2,3,4,5,6]], ndmin=3)
# print(arr1)
# print(arr1.shape)

# test = np.array([[1,2,3,4,5,6],[3,4,5,6,7,9]])
# new_test = test.reshape(-1)
# print(new_test)

# two_d_arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# for i in two_d_arr:
#     for j in i:
#         print(j)

# two_d_arr = np.array([1,2,3,4,5,6,7,8,9,10])
# for a in np.nditer(two_d_arr, flags=['buffered'], op_dtypes=['S']):
#     print(a)

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr)
# for i in np.nditer(arr[:,1::2]):
#     print(i)

for i,j in np.ndenumerate(arr):
    print(i,j)

a = [10,20,30,40,50]

for i,j in enumerate(a):
    print(i,j)