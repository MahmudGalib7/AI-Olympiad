def hashFunction(element):
    return sum(ord(char) for char in element) % 10

def hashContains(name, arr):
    index = hashFunction(name)
    return arr[index] == name

def hashAddElement(value, arr):
    index = hashFunction(value)
    if arr[index] == value:
        return True
    else:
        arr.insert(index, value)
        return False