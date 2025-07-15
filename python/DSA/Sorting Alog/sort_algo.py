arr = [3, 4, 5, 1, 7]

n = len(arr)
for i in range(n-1):
    mn = i
    for j in range(i+1, n):
        if arr[j] < arr[mn]:
            mn = j
    arr[mn], arr[i] = arr[i], arr[mn]
    
print(arr)