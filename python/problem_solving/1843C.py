def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        total = 0
        while n:
            total += n
            n //= 2
        print(total)

solve()

# 2x -> left where right is 2x+1
# 3 -> 3 + 1 -> 4
# 10 -> 10 + 5 + 2 + 1 -> 18
# 1 -> 1 + 0 -> 0