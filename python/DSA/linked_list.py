"""
data       3    5    7
---- ->  ---- ---- ----
Node      N1   N2   N3
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

n1 = Node(10)
n2 = Node(1000)
n3 = Node(100)
n4 = Node(200)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

current_node = n1

while current_node:
    print(current_node.data, end = " -> ")
    current_node = current_node.next

print("Null")