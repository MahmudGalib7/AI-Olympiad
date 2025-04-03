x = int(input().strip())

# Calculate minimum steps using integer division and modulus
steps = (x // 5) + (1 if x % 5 != 0 else 0)

print(steps)
