n = int(input())

x_total = 0
y_total = 0
z_total = 0

for _ in range(n):
    x, y, z = map(int, input().split())
    x_total += x
    y_total += y
    z_total += z

if x_total == 0 and y_total == 0 and z_total == 0:
    print("YES")
else:
    print("NO")
