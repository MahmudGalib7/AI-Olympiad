from sample_data import name
from hashset import HashSet
from hashmap import HashMap

print("-- HashSet Test --")
hashset = HashSet(size=10)
for n in name:
    hashset.hashAddElement(n)
hashset.show()
hashset.hashRemoveElement('bob')
hashset.show()

print("-- HashMap Test --")
hashmap = HashMap(size=10)
hashmap.put("1", 'musk')
hashmap.put("2", 'Light')
hashmap.put("4", 'Johan')
hashmap.put("7", 'John')
hashmap.put("6", 'Miles')
hashmap.put("3", 'Elon')
hashmap.put("2", 'tatsuya')

hashmap.show()
hashmap.get("4")
hashmap.remove("1")
hashmap.show()