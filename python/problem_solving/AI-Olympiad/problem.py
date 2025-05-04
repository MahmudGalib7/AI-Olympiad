# import math

# def solve():
#     m, n, d = map(int, input().split())
#     speed_component = math.sqrt(m**2 + n**2)
#     if speed_component == 0:
#         time_hours = 0
#     else:
#         time_hours = d / speed_component
#     time_minutes = time_hours * 60
#     print(f"{time_minutes:.8f}")

# t = int(input())
# for i in range(t):
#     solve()

# import sys
# input_line = sys.stdin.readline()
# print("".join(input_line), end="")

# import sys
# def solve():
#     s = sys.stdin.readline().strip()
#     n = len(s)
#     found = False

#     for i in range(n -1):
#         if s[i] == s[i+1]:
#             print(f"{i+1} {i+2}")
#             found = True
#             break
#     if found:
#         return
    
#     for i in range(n - 2):
#         if s[i] == s[i+2]:
#             print(f"{i + 1} {i + 3}")
#             found = True
#             break
    
#     if not found:
#         print("-1 -1")
# solve()

# import math
# import sys

# input = sys.stdin.readline
# def gcd(a,b):
#     while b:
#         a,  b = b, a % b
#     return abs(a)
# a, b, x, y = map(int, input().split())
# com_d = gcd(x,y)
# x_simp = x // com_d
# y_simp = y // com_d
# max_k_a = a // x_simp
# max_k_b = b // y_simp
# result = min_max_k_a, max_k_b)
# print(result)

# import sys

# inp = sys.stdin.readline

# def sol():
#     n = int(input())
#     h = list(map(int, input().split()))

#     curr_eng = 0
#     max_d = 0

#     for i in range(n-1):
#         diff = h[i+1] - h[i]
#         curr_eng -= diff
#         max_d = max(max_d, -curr_eng)
#     print(max_d)
# sol()

# import sys
# inp = sys.stdin.readline
# def sol():
#     n = int(input())
#     coins = list(map(int, input().split()))
#     poss_s = {0}
#     for c in coins:
#         new_s = set()
#         for exis_s in poss_s:
#             new_s.add(exis_s + c)
#         poss_s.update(new_s)
#     if 0 in poss_s:
#         poss_s.remove(0)
#     sort_s = sorted(list(poss_s))
#     print(len(sort_s))
#     print(*sort_s)

# sol()


# import sys
# inp = sys.stdin.readline
# def check(time, ser_t, tar_i):
#     if time < 0:
#         return False
#     total_i = 0
#     for i in ser_t:
#         total_i += time // i
#         if total_i >= tar_i:
#             return True
#     return False
# def sol():
#     n, t = map(int, input().split())
#     ser_t = list(map(int, input().split()))
#     if t == 0:
#         print(0)
#         return
#     low = 0
#     min_k = min(ser_t)
#     high = min_k * t
#     min_req_t = high

#     while low <= high:
#         mid = low + (high - low) // 2
#         if check(mid, ser_t, t):
#             min_req_t = mid
#             high = mid - 1
#         else:
#             low = mid + 1
#     print(min_req_t)
# sol()

# import sys
# inp = sys.stdin.readline

# def sol():
#     n = int(input())
#     a = list(map(int, input().split()))
#     max_req_h = 0
#     sum_a = 0
#     for i in range(n):
#         req_h = a[i] - i
#         max_req_h = max(max_req_h, req_h)
#         sum_a += a[i]
#     h_min = max_req_h
#     sum_indices = n * (n - 1) // 2
#     total_p = (n * h_min) + sum_indices - sum_a
#     print(total_p)
# sol()

# import sys
# inp = sys.stdin.readline
# def find(i, par):
#     if par[i] == i:
#         return i
#     par[i] = find(par[i], par)
#     return par[i]
# def union(i, j, par):
#     root_i = find(i, par)
#     root_j = find(j, par)
#     if root_i != root_j:
#         par[root_i] = root_j
#         return True
#     else:
#         return False
# def sol():
#     n, m = map(int, input().split())
#     par = [i for i in range(n + 1)]
#     cycle = False
#     for j in range(m):
#         u, v = map(int, input().split())
#         if not union(u, v, par):
#             cycle = True
#     if cycle:
#         print("YES")
#     else:
#         print("NO")
# x=int(input())
# for _ in range(x):
#     sol()



from collections import deque
import sys
inp = sys.stdin.readline

def sol():
    m, n, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    queue = deque()
    conq_day = [[-1]*n for _ in range(m)]
    init = 0
    conq_count = 0
    dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                init += 1
            elif grid[r][c] == 2:
                queue.append((r, c))
                conq_day[r][c] = 0
    while queue:
        r, c = queue.popleft()
        curr_day = conq_day[r][c]
        for dr, dc in dir:
            nr, nc = r+dr, c+dc
            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and conq_day[nr][nc] == -1:
                next_day = curr_day + 1
                conq_day[nr][nc] = next_day
                conq_count += 1
                queue.append((nr, nc))
    if conq_count != init:
        print(0)
    else:
        result_k = 0
        for r in range(m):
            for c in range(n):
                if conq_day[r][c] == k:
                    result_k += 1
        print(1, result_k)
sol()