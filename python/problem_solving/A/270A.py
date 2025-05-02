t = int(input())
inputs = [int(input()) for _ in range(t)]

for n in inputs:
    if 360 % (180 - n) == 0:
        print("YES")
    else:
        print("NO")
