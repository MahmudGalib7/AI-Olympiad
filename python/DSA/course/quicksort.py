a = [12,7,64,32,24,29,55,2]

def partition(arr, high, low):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def QuickSort(arr, low=0, high=None):
    n = len(arr)
    if high is None:
        high = n - 1

    if low < high:
        p_index = partition(arr, high, low)
        QuickSort(arr, low, p_index-1)
        QuickSort(arr, p_index+1, high)

QuickSort(a)
print(a)