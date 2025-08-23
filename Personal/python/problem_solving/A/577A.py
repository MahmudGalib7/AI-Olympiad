n, x = map(int, input().split())
count = 0

for i in range(1, n + 1):
    if x % i == 0:
        j = x // i
        if j <= n:
            count += 1

print(count)
