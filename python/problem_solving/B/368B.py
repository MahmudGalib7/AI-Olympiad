n, m = map(int , input().split())
a = list(map(int, input().split()))
seen = set()

unique_count = [0] * n
for i in range(n-1, -1, -1):
    seen.add(a[i])
    unique_count[i] = len(seen)

for j in range(m):
    l = int(input())
    print(unique_count[l-1])