from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = defaultdict(int)
    total = 0

    for i in range(n):
        key = a[i] - i
        count[key] += 1
    for val in count.values():
        total += val * (val - 1) // 2

    print(total)
