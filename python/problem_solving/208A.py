s = input().strip()

words = s.split('WUB')
valid_words = []

for word in words:
    if word:
        valid_words.append(word)

original_string = ' '.join(valid_words)
print(original_string)
