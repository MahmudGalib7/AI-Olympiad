numbers = [4, 3, 7, 3, 2]

# 1st way
print(3 in numbers)

#2nd way
print(numbers.index(3))

#3rd way
def count(items, target):
    result = 0
    for item in items:
        if item == target:
            result += 1
    return result

print(count(numbers, 3))
