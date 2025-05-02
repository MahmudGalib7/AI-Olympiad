n, m, a, b = map(int, input().split())

option_one = n * a
option_two = ((n + m - 1) // m) * b
option_three = (n // m) * b + (n % m) * a

print(min(option_one, option_two, option_three))
