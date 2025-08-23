import numpy as np

arr1 = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
arr2 = np.array([[4,5,6],[10,11,12]])
arr3 = np.array([13,14,15,16,17,18,19,20])
arr4 = np.array([16,17])

# joint_arr1_2 = np.concatenate((arr1,arr2), axis=1)
# joint_arr3_4 = np.stack((arr3,arr4))
# joint_arr3_4 = np.hstack((arr3,arr4))
# joint_arr3_4 = np.vstack((arr3,arr4))
# joint_arr3_4 = np.dstack((arr3,arr4))
# print(joint_arr3_4)

# split_arr3_4 = np.array_split(arr3, 3)
# print(split_arr3_4)
# print(split_arr3_4[0])

split_arr1_2 = np.split(arr1, 3)
print(split_arr1_2)