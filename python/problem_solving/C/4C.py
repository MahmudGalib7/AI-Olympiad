t = int(input())
ok = []
count = {}
for i in range(t):
    s = input()

    if s not in count:
        print("OK")
        count[s] = 0
        ok.append(s)
    else:
        count[s] += 1
        new_name = f'{s}{count[s]}'
        while new_name in count:
            count[s] += 1
            new_name = f'{s}{count[s]}'
        ok.append(new_name)
        print(new_name)