n, m = map(int, input().split())
pieces = list(map(int, input().split()))

pieces.sort()

min_diff = float('inf')

for i in range(m - n + 1):
    diff = pieces[i + n - 1] - pieces[i]
    if diff < min_diff:
        min_diff = diff

print(min_diff)
