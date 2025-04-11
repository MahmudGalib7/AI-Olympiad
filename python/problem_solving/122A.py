def is_lucky(num):
    return all(ch in '47' for ch in str(num))


n = int(input())
found = False

for i in range(1, n + 1):
    if is_lucky(i) and n % i == 0:
        found = True
        break

print("YES" if found else "NO")
