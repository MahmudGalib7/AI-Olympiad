n, a, b, c = map(int, input().split())


def max_ribbons(n, a, b, c):
    dp = [float('-inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if i >= a and dp[i - a] != float('-inf'):
            dp[i] = max(dp[i], dp[i - a] + 1)

        if i >= b and dp[i - b] != float('-inf'):
            dp[i] = max(dp[i], dp[i - b] + 1)

        if i >= c and dp[i - c] != float('-inf'):
            dp[i] = max(dp[i], dp[i - c] + 1)
    return dp[i]

print(max_ribbons(n, a, b, c))
