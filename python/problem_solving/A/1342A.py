t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    min_xy = min(x, y)
    diff = abs(x - y)

    if b < 2 * a:
        print(min_xy * b + diff * a)
    else:
        print((x + y) * a)
