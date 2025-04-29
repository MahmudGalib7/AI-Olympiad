n = int(input())
p = list(map(int, input().split()))

path = []
q = [0] + [0] + p
current = n

while current != 1:
    path.append(current)
    current = q[current]

path.append(1)
path.reverse()
print(*path)