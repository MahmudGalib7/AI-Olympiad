n, t = map(int, input().split())
count = 0
a = list(map(int, input().split()))

for num in a:
    if num > t:
        count += 1

print(count)
