n, m = map(int, input().split())

tasks = list(map(int, input().split()))

current_house = 1

total_time = 0

for task in tasks:
    if task >= current_house:
        total_time += task - current_house
    else:
        total_time += (n - current_house) + task

    current_house = task

print(total_time)
