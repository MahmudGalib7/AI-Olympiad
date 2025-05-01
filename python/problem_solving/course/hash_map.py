nums = list(map(int, input().split()))
target = int(input())

# for num in nums:
#     if target - num in nums:
#         index1 = nums.index(num)
#         index2 = nums.index(target - num)
#         print([index1, index2])
#         break
# else:
#     print(-1)

def two_sum(num, target):
    seen_number = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen_number:
            return [seen_number[complement], i]
        seen_number[num] = i
    return []

result = two_sum(nums, target)
if result:
    print(result)
else:
    print(-1)