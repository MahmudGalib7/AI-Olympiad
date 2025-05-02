t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    balance = 0
    min_balance = 0

    for ch in s:
        if ch == '(':
            balance += 1
        else:
            balance -= 1
        min_balance = min(min_balance, balance)

    print(-min_balance)
