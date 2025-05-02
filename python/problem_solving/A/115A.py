import sys
sys.setrecursionlimit(10000)

n = int(input())
p = list(map(int, [input() for _ in range(n)]))

depth = [0] * n

def find_depth(i):
    if depth[i]:
        return depth[i]
    if p[i] == -1:
        depth[i] = 1
    else:
        depth[i] = 1 + find_depth(p[i]-1)
    return depth[i]

ans = 0
for i in range(n):
    ans = max(ans, find_depth(i))

print(ans)
