s = input()
uppercase_count = 0
lowercase_count = 0

for i in s:
    if i.isupper():
        uppercase_count += 1
    else:
        lowercase_count += 1

if uppercase_count > lowercase_count:
    print(s.upper())
else:
    print(s.lower())
