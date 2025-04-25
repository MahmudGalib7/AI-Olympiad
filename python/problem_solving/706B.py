from bisect import bisect_right

n = int(input())
prices = list(map(int, input().split()))
prices.sort()

q = int(input())
days = [int(input()) for _ in range(q)]

for money in days:
    count = bisect_right(prices, money)
    print(count)
