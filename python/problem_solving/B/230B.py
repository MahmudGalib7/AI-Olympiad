import math

MAX_N_SQRT = 1000001
is_prime = [True] * MAX_N_SQRT
is_prime[0] = is_prime[1] = False

for p in range(2, int(math.sqrt(MAX_N_SQRT)) + 1):
    if is_prime[p]:
        for i in range(p * p, MAX_N_SQRT, p):
            is_prime[i] = False

n = int(input())
t = list(map(int, input().split()))

for x in t:
    if x <= 1:
        print("NO")
        continue

    sqrt_x = math.isqrt(x)

    if sqrt_x * sqrt_x == x and is_prime[sqrt_x]:
        print("YES")
    else:
        print("NO")
