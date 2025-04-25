n, k = map(int, input().split())
heights = list(map(int, input().split()))

current_sum = sum(heights[:k])
min_sum = current_sum
min_index = 0

for i in range(1, n - k + 1):
    current_sum = current_sum - heights[i - 1] + heights[i + k - 1]

    if current_sum < min_sum:
        min_sum = current_sum
        min_index = i
print(min_index + 1)
