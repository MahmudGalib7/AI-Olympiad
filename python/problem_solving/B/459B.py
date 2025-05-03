n = int(input())
b = list(map(int, input().split()))

max_diff = max(b) - min(b)
count = 0

if max_diff == 0:
    count  = n * (n - 1) // 2
else:
    min_count = b.count(min(b))
    max_count = b.count(max(b))
    count = min_count * max_count
print(max_diff, count)