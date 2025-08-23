n, k = map(int, input().split())

odd_count = (n + 1) // 2
if k <= odd_count:
    print(2 * k - 1)
else:
    k -= odd_count
    print(2 * k)
