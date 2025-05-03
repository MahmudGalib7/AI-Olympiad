class HashMap:
    def __init__(self, initial_size=10):
        # Initialize the array (list) of buckets. Each bucket is initially an empty list.
        self.buckets = [[] for _ in range(initial_size)]
        self.size = initial_size
        self.count = 0 # Keep track of number of elements

    def _hash_function(self, key):
        # A simple hash function using Python's built-in hash()
        # Modulo ensures the index is within the bounds of our bucket list
        return hash(key) % self.size

    def put(self, key, value):
        # Calculate the index for the key
        index = self._hash_function(key)
        # Get the bucket (list) at this index
        bucket = self.buckets[index]
        # Check if the key already exists in the bucket
        found = False
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                # Key found, update the value
                bucket[i] = (key, value)
                found = True
                break

        # If key was not found, append the new (key, value) pair
        if not found:
            bucket.append((key, value))
            self.count += 1

        # Optional: Add logic here to resize the hashmap if it gets too full
        # (e.g., if self.count / self.size > 0.7)

    def get(self, key):
        # Calculate the index for the key
        index = self._hash_function(key)
        # Get the bucket (list) at this index
        bucket = self.buckets[index]

        # Search for the key in the bucket
        for existing_key, existing_value in bucket:
            if existing_key == key:
                # Key found, return the value
                return existing_value

        # If the loop finishes without finding the key
        raise KeyError2(f"Key '{key}' not found in HashMap") # Or return None

    def remove(self, key):
        # Calculate the index for the key
        index = self._hash_function(key)
        # Get the bucket (list) at this index
        bucket = self.buckets[index]

        # Search for the key to remove
        original_len = len(bucket)
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                # Key found, remove the tuple using list pop or del
                del bucket[i]
                self.count -= 1
                return # Exit after removing

        # If the loop finishes, the key wasn't found
        raise KeyError(f"Key '{key}' not found in HashMap")

    def __str__(self):
        # For printing the HashMap contents (optional)
        items = []
        for bucket in self.buckets:
            if bucket: # Only include non-empty buckets for clarity
                items.append(str(bucket))
        return "{" + ", ".join(items) + "}"

    def __len__(self):
        # Return the number of key-value pairs stored
        return self.count

# --- Example Usage ---
my_map = HashMap(5) # Create a map with 5 initial buckets

my_map.put("apple", 1)
my_map.put("banana", 2)
my_map.put("cherry", 3)
my_map.put("date", 4) # Potential collision depending on hash function

print(f"Map: {my_map}")
print(f"Size: {len(my_map)}")

# Get values
print(f"Value for 'banana': {my_map.get('banana')}")
# print(f"Value for 'grape': {my_map.get('grape')}") # This would raise KeyError

# Update value
my_map.put("apple", 10)
print(f"Updated value for 'apple': {my_map.get('apple')}")
print(f"Map after update: {my_map}")

# Remove value
my_map.remove("cherry")
print(f"Map after removing 'cherry': {my_map}")
print(f"Size after remove: {len(my_map)}")

# Test collision (depends on hash function, 'apple' and 'date' might collide)
my_map.put("fig", 5)
print(f"Map after adding 'fig': {my_map}")