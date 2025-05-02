def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        c1 = s.count('-')
        c2 = s.count('_')

        max_ans = 0
        for i in range(c1 + 1):
            # Place i dashes before underscores, rest after
            left = i
            right = c1 - i
            max_ans = max(max_ans, left * c2 * right)

        print(max_ans)


solve()
