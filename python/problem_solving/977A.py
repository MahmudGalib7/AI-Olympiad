number, k = map(int, input().split())

for i in range(k):
    if str(number)[-1] == '0':
        number //= 10
    else:
        number -= 1

print(number)
