s = input()
target = "hello"
i = 0

for char in s:
    if char == target[i]:
        i += 1
        if i == len(target):
            break

if i == len(target):
    print("YES")
else:
    print("NO")
