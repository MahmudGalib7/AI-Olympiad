nums = list(map(int, input().split()))
k = int(input())

nums.sort()
if 1 <= k <= len(nums):
    print(nums[-k])
else:
    print("k is out of bounds")