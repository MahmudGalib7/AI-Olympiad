k, n, w = map(int, input().split())
l = 0
for i in range(w):
    l += k*(i+1)

print(l-n if l > n else 0)
