# NOT SOLVABLE USING PYTHON

n, q = map(int, input().split())
deck = list(map(int, input().split()))
queries = list(map(int, input().split()))

color_pos = dict()
for idx, color in enumerate(deck):
    if color not in color_pos:
        color_pos[color] = idx

output = []

for t in queries:
    pos = color_pos[t] + 1
    output.append(pos)

    for color in color_pos:
        if color_pos[color] < color_pos[t]:
            color_pos[color] += 1
    color_pos[t] = 0

print(*output)