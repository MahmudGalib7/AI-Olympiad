# Hash Map

"""
step 1 -> Create an array
step 2 -> Create a hash function
step 3 -> store array info in hash function
step 4 -> Handling positions
step 5 -> Will search for an element from the array
"""

# Sample Data
arr = [12, 7, 64, 32, 24, 29, 55, 2]
name = ['alex', 'bob', 'siri', 'david', 'elon']

# OOP


class HashSet():
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for i in range(size)]

    def hashFunction(self, element):
        sum_of_value = 0
        for item in element:
            sum_of_value += ord(item)
        return sum_of_value % len(self.buckets)

    def hashContains(self, name):
        index = self.hashFunction(name)
        return self.buckets[index] == name

    def hashAddElement(self, value):
        index = self.hashFunction(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    def hashRemoveElement(self, value):
        index = self.hashFunction(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    def show(self):
        print("This is Hash Set contains")
        for index, value in enumerate(self.buckets):
            print(index, value)

# Basic

# def hashFunction(element):
#     sum_of_value = 0
#     for item in element:
#         sum_of_value += ord(item)
#
#     return su_of_value % len(elementm)
#
# def hashContains(name, arr):
#     index = hashFunction(name)
#     return arr[index] == name
#
# def hashAddElement(value, arr):
#     index = hashFunction(value)
#     if arr[index] == value:
#         return arr[index] == value
#     else:
#         return arr.insert(index, value)
#
# for element in name:
#     test.insert(hashFunction(element), element)

# Test

# print(test)
# print(hashContains('musk', test))
# print(hashAddElement('musk', test))
# print(test)


test = HashSet(size=10)
for element in name:
    test.hashAddElement(element)

# Adding elements

print(test.hashAddElement('musk'))
print(test.hashAddElement('mark'))
print(test.hashAddElement('william'))
print(test.hashAddElement('johan'))
print(test.hashAddElement('smith'))
print(test.hashAddElement('cid'))
print(test.hashAddElement('jack'))
print(test.hashAddElement('tatsuya'))
print(test.hashAddElement('Light'))

# Removing elements

print(test.hashRemoveElement('musk'))

# printing the hashset

print(test.show())

# Testing unicode & hash position/index

# items = ['david', 'elon']
# sum_of_unicode = 0
# for name in items:
#     print(f"{name}:")
#     for char in name:
#         sum_of_unicode += ord(char)
#         print(f"  '{char}' -> {ord(char)}")
#     print(f" '{name}' -> {sum_of_unicode}")
#     index = sum_of_unicode % len(items)
#     print(f"Hash Index -> {index}")
