a = [12,7,64,32,24,29,55,2]

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

print(linearSearch(a, 25))