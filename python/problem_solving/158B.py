from collections import Counter

n = int(input())
group = list(map(int, input().split()))

count = Counter(group)
taxis = 0

taxis += count[4]

pairs = min(count[3], count[1])
taxis += pairs
count[3] -= pairs
count[1] -= pairs

taxis += count[3]

taxis += count[2] // 2
if count[2] % 2:
    taxis += 1
    count[1] -= min(2, count[1])

if count[1] > 0:
    taxis += (count[1] + 3) // 4

print(taxis)
