def find_kth_non_divisible(n, k):
    left, right = 1, 2 * k
    while left < right:
        mid = (left + right) // 2
        if mid - mid // n < k:
            left = mid + 1
        else:
            right = mid
    return left


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(find_kth_non_divisible(n, k))
