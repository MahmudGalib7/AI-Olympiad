n, t = map(int, input().split())

if n == 1 and t == 10:
    print(-1)
else:
    if t == 10:
        print('1' + '0' * (n - 1))
    else:
        print(str(t) + '0' * (n - len(str(t))))
