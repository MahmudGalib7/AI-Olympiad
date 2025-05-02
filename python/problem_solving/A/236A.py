s = list(map(str, input().strip()))

result = []

for i in s:
    if i not in result:
        result.append(i)

if len(result) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
