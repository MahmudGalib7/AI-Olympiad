x = input().strip()
res = ""

for i in range(len(x)):
    d = int(x[i])
    if i == 0 and d == 9:
        res += x[i]
    else:
        res += str(min(d, 9 - d))

print(res)
