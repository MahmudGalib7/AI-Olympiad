s, n = map(int, input().split())

dragons = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    dragons.append((x1, x2))

dragons.sort(key=lambda dragon: dragon[0])

for dragon in dragons:
    x1, x2 = dragon
    if s > x1:
        s += x2
    else:
        print("NO")
        break
else:
    print("YES")
