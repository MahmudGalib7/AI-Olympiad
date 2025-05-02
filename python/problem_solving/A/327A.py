n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(0 if a[0] == 1 else 1)
else:
    total_ones = sum(a)
    max_gain = float('-inf')
    current_gain = 0

    for i in range(n):
        val = 1 if a[i] == 0 else -1
        current_gain = max(val, current_gain + val)
        max_gain = max(max_gain, current_gain)

    print(total_ones + max_gain)
