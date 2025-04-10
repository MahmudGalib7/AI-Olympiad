word = input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']

result = ""

for i in word:
    if i.lower() not in vowels:
        result += '.'+i.lower()

print(result)
