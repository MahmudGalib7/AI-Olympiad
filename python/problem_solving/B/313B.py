s = input().strip()
n = len(s)

m = int(input().strip())

equal = [0] * (n-1)
for i in range(n-1):
    if s[i] == s[i+1]:
        equal[i] = 1

prefix_sum = [0] * n
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1] + equal[i-1]

results = []
for _ in range(m):
    l, r = map(int, input().strip().split())
    l -= 1
    r -= 1
    results.append(prefix_sum[r] - prefix_sum[l])

for result in results:
    print(result)
