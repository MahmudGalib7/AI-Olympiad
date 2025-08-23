n = int(input())
score = {}

for _ in range(n):
    team = input()
    if team in score:
        score[team] += 1
    else:
        score[team] = 1

winner = max(score, key=score.get)
print(winner)
