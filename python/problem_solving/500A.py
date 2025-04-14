n, t_cell = map(int, input().split())
cells = list(map(int, input().split()))

pos = 1
while pos < t_cell:
    pos += cells[pos - 1]

if pos == t_cell:
    print("YES")
else:
    print("NO")
