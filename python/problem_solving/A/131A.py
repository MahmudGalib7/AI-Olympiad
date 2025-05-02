word = input()

if len(word) == 1 and word == word.upper():
    print(word.lower())
elif len(word) == 1 and word == word.lower():
    print(word.upper())
else:
    if word.isupper():
        print(word.lower())
    elif word[1:].isupper() and word[0].islower():
        print(word.capitalize())
    else:
        print(word)
