a = [12,7,64,32,24,29,55,2]

def selectionSort(arr):
    n = len(arr)

    for i in range(n - 1):
        minimum_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[minimum_index]:
                minimum_index = j

        # minimum_value = arr.pop(minimum_index)
        # arr.insert(i, minimum_value)
        arr[i], arr[minimum_index] = arr[minimum_index], arr[i]

    return arr

print(selectionSort(a))