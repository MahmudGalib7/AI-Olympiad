n = int(input())
nums = list(map(int, input().split()))

even = 0
odd = 0
index_even = -1
index_odd = -1

for i, num in enumerate(nums):
    if num % 2 == 0:
        even += 1
        index_even = i
    else:
        odd += 1
        index_odd = i

if even == 1:
    print(index_even + 1)
else:
    print(index_odd + 1)