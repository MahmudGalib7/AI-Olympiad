t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()

    a_ones = b_ones = 0
    flip = False
    possible = True

    for i in range(n):
        if flip:
            # If we've flipped earlier, simulate it
            a_i = '1' if a[i] == '0' else '0'
        else:
            a_i = a[i]

        if a_i != b[i]:
            if a_ones == b_ones:
                flip = not flip  # Flip the prefix
            else:
                possible = False
                break

        a_ones += int(a[i])
        b_ones += int(b[i])

    print("YES" if possible else "NO")
