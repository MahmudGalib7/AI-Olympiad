n, h = map(int, input().split())
p = list(map(int, input().split()))
width = 0

for i in range(n):
    if h >= p[i]:
        width += 1
    else:
        width += 2

print(width)
