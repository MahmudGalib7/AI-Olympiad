last_digits = [6, 8, 4, 2]
n = int(input())
if n > 0:
    print(last_digits[n % 4])
else:
    print(1)
