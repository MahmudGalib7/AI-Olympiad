"""
i -> int
b -> boolean
u -> unsigned int
c -> complex plot
m -> time
M -> date & time
O -> object
S -> string
U -> uni-code string
V -> memory for other type

"""

import numpy as np

test = np.array([1,2,3,4,5,6,7,8,9,10], dtype='i4')

# print(test.dtype)
# print(test)
#
# new_test = test.astype('S')
# print(new_test.astype(str).astype('U'))
# print(new_test.dtype)
#
# arr = np.array([1,2,3,4,5,0,-1])
# new_arr = arr.astype(bool)
# print(new_arr)

cp_test = test.copy() # copy owns data
# cp_test[0] = 100
# print(cp_test)
# print(test)

view_test = test.view() # view doesnt own data
# view_test[0] = 100
# print(view_test)
# print(test)

print(cp_test.base) # the copy returns none
print(view_test.base) # the view returns the original array