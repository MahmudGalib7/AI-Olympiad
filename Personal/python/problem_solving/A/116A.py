n = int(input())
max_capacity = 0
current_passanger = 0

for i in range(n):
    a, b = map(int, input().split())
    current_passanger -= a
    current_passanger += b

    if current_passanger > max_capacity:
        max_capacity = current_passanger

print(max_capacity)
