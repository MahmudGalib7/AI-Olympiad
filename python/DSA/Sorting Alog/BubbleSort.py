arr = [12,7,64,32,24,29,55,2]

def bubbleSort(arr):
    n = len(arr)
    swap = False

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

                swap = True
            if not swap:
                break

    return arr

print(bubbleSort(arr)[0])