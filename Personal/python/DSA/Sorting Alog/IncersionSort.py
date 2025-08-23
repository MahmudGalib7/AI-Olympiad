a = [12,7,64,32,24,29,55,2]

def IncersionSort(arr):
    n = len(arr)

    for i in range(1, n):
        insert_index = i
        current_value = arr.pop(i)

        for j in range(i-1, -1, -1):
            if arr[j] > current_value:
                insert_index = j
        # arr.insert(insert_index, current_value)

    return arr

print(IncersionSort(a))