n = int(input())
v = list(map(int, input().split()))

original_prefix = [0] * (n + 1)
sorted_v = sorted(v)
sorted_prefix = [0] * (n + 1)

for i in range(n):
    original_prefix[i + 1] = original_prefix[i] + v[i]
    sorted_prefix[i + 1] = sorted_prefix[i] + sorted_v[i]

m = int(input())
for _ in range(m):
    type_, l, r = map(int, input().split())
    if not (1 <= l <= r <= n):
        continue

    if type_ == 1:
        print(original_prefix[r] - original_prefix[l - 1])
    else:
        print(sorted_prefix[r] - sorted_prefix[l - 1])
