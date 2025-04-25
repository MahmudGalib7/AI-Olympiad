class HashSet:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hashFunction(self, element):
        return sum(ord(c) for c in element) % self.size

    def hashContains(self, name):
        index = self.hashFunction(name)
        return name in self.buckets[index]

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
        print("HashSet Contents:")
        for index, value in enumerate(self.buckets):
            print(f"{index}: {value}")
