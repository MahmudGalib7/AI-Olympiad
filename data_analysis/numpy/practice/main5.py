import numpy as np

arr1d = np.array([10,1,8,7,3,4,9,5,6,2])
filter_arr = arr1d % 2 == 0
# for e in arr1d:
#     if e > 5:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
#
print(filter_arr)

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# print(np.where(arr1d >= 4))
# print(np.where(arr1d % 2 != 0))

# print(np.sort(arr1d))
# print(np.sort(arr2d))
# print(np.sort(arr3d))

arr_str = np.array(['banana', 'cherry', 'apple'])
# print(np.sort(arr_str))

arr_bool = np.array([True, True, False])
# print(np.sort(arr_bool))

int_arr_1 = np.array([1,2,3])
int_arr_2 = np.array([4,5,6])

new_arr = int_arr_1[arr_bool]
# print(new_arr)