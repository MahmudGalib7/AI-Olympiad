n, m = map(int, input().split())

min_moves = (n + 1) // 2  # same as ceil(n / 2)

for moves in range(min_moves, n + 1):
    if moves % m == 0:
        print(moves)
        break
else:
    print(-1)
