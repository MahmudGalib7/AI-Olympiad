a = int(input())
b = int(input())
c = int(input())

results = [
    a + b + c,
    a + b * c,
    a * b + c,
    a * b * c,
    (a + b) * c,
    a * (b + c)
]

print(max(results))
