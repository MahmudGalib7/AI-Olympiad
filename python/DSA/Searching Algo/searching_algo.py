# Linear searching algorithm

# a = [12,7,64,32,24,29,55,2]
#
# def linearSearch(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i

#     return -1
#
# print(linearSearch(a, 25))

# Binary search algorithm

# a = [12,7,64,32,24,29,55,2]
#
# def binarySearch(arr, target):
#     left = 0
#     right = len(arr) - 1
#
#     while left <= right:
#         mid = (left+right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return -1
#
# a.sort()
# print(binarySearch(a, 55))
