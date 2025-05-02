t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    # if n >= 2*k and n % 2 == 0:
    #     print("YES")
    #     print("2 " * (k - 1) + str(n - 2 * (k - 1)))
    # elif n >= k and n % 2 == k % 2:
    #     print("YES")
    #     print("1 " * (k - 1) + str(n - (k - 1)))
    # else:
    #     print("NO")

    if n >= 2*k and (n - 2 * k) % 2 == 0:
        print("YES")
        print("2 " * (k - 1) + str(n - 2 * (k - 1)))
    elif n >= k and (n - k) % 2 == 0:
        print("YES")
        print("1 " * (k - 1) + str(n - (k - 1)))
    else:
        print("NO")