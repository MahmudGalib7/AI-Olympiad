class HashMap:
    def __init__(self, size):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def hashFunction(self, element):
        sum_of_value = sum(int(char) for char in element if char.isdigit())
        return sum_of_value % self.size

    def put(self, key, value):
        index = self.hashFunction(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        index = self.hashFunction(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if key == k:
                print(f"{key}: {v}")
                return v
        print(f"{key}: Not found")
        return None

    def remove(self, key):
        index = self.hashFunction(key)
        bucket = self.buckets[index]
        for i, (k, _) in enumerate(bucket):
            if key == k:
                del bucket[i]
                return
        print("Value not found")

    def show(self):
        print("HashMap Contents:")
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")