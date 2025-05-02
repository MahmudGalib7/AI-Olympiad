n = int(input())
a = input().strip()

count = 0

for i in range(n - 1):
    if a[i] == a[i + 1]:  # Check if current character is the same as the next one
        count += 1

print(count)
