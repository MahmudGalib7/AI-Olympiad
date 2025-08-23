import numpy as np

arr = np.array([[1,2,3,4,5], [2,3,4,5,6]])
# print(arr[1,4]) # get 6

z = np.array([[[1,2,3], [4,5,6]],[[7,8,9], [10,11,12]],[[13,14,15], [16,17,18]]], dtype='S')
print(z[2,1,1]) # get 17

abc = [10,20,30,40,50,607,60]
# print(abc[-1:-4:-1])
# print(abc[::-1])
# print(abc[::2])

qwe= np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
# print(qwe[0:2,2])
# print(qwe[0:3,1])

print(z.dtype)