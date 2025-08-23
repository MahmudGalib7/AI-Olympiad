n, l = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()

max_gap = 0
for i in range(1, n):
    max_gap = max(max_gap, positions[i] - positions[i - 1])

start_gap = positions[0]
end_gap = l - positions[-1]

d = max(max_gap / 2, start_gap, end_gap)
print(f"{d:.10f}")
