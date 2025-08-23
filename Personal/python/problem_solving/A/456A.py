n = int(input())
laptops = []

for _ in range(n):
    price, quality = map(int, input().split())
    laptops.append((price, quality))

laptops.sort()

for i in range(1, n):
    if laptops[i][1] < laptops[i - 1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
