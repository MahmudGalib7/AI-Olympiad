# arr = [12,7,64,32,24,29,55,2]
from more_itertools.recipes import partition

# def bubbleSort(arr):
#     n = len(arr)
#     swap = False
#
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
#                 swap = True
#             if not swap:
#                 break
#
#     return arr
#
# print(bubbleSort(arr)[0])

# a = [12,7,64,32,24,29,55,2]

# def selectionSort(arr):
#     n = len(arr)
#
#     for i in range(n - 1):
#         minimum_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[minimum_index]:
#                 minimum_index = j
#
#         # minimum_value = arr.pop(minimum_index)
#         # arr.insert(i, minimum_value)
#         arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
#
#     return arr

# print(selectionSort(a))

# a = [12,7,64,32,24,29,55,2]
#
# def IncersionSort(arr):
#     n = len(arr)
#
#     for i in range(1, n):
#         insert_index = i
#         current_value = arr.pop(i)
#
#         for j in range(i-1, -1, -1):
#             if arr[j] > current_value:
#                 insert_index = j
#         # arr.insert(insert_index, current_value)
#
#     return arr
#
# print(IncersionSort(a))

# Quick sort

# a = [12,7,64,32,24,29,55,2]
#
# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#
#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i+1
#
#
# def QuickSort(arr, low=0, high=None):
#     n = len(arr)
#     if high is None:
#         high = n - 1
#
#     if low < high:
#         p_index = partition(arr, low, high)
#         QuickSort(arr, low, p_index-1)
#         QuickSort(arr, p_index+1, high)
#
#
# QuickSort(a)
# print(a)