"""
data       3    5    7
---- ->  ---- ---- ----
Node      N1   N2   N3
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


n1 = Node(10)
n2 = Node(1000)
n3 = Node(100)
n4 = Node(200)
n5 = Node(50)

n1.next = n2
n2.previous = n1
n2.next = n3
n3.previous = n2
n3.next = n4
n4.previous = n3
n4.next = n5
n5.previous = n4

# normal doubled linked list

# current_node = n1
# while current_node:
#     if current_node.next:
#         print(f"data: {current_node.data}, address: {
#               id(current_node)}, next_address: {id(current_node.next)} \n", end=" -> ")
#     else:
#         print(f"data: {current_node.data}, address: {
#               id(current_node)}, next_address: None")
#     current_node = current_node.next
# print("---------------------------------------------------------------------------------------------------------------")
#
# print("FORWARD VS BACKWARD")
#
# print("---------------------------------------------------------------------------------------------------------------")
# current_node = n5
#
# while current_node:
#     if current_node.previous:
#         print(f"data: {current_node.data}, address: {id(current_node)}, prev_address: {
#               id(current_node.previous)} \n", end=" -> ")
#     else:
#         print(f"data: {current_node.data}, address: {
#               id(current_node)}, prev_address : None")
#     current_node = current_node.previous

# circular doubled linked list

n1.previous = n5
n5.next = n1

current_node = n1
print(f"data: {current_node.data}, address: {
              id(current_node)}, next_address: {id(current_node.next)} \n", end=" -> ")
start_node = n1
current_node = current_node.next
while current_node != start_node:
    if current_node.next:
        print(f"data: {current_node.data}, address: {
              id(current_node)}, next_address: {id(current_node.next)} \n", end=" -> ")
    else:
        print(f"data: {current_node.data}, address: {
              id(current_node)}, next_address: None")
    current_node = current_node.next

print("\n---------------------------------------------------------------------------------------------------------------")

print("\nFORWARD VS BACKWARD")

print("\n---------------------------------------------------------------------------------------------------------------")

current_node = n5
print(f"data: {current_node.data}, address: {
              id(current_node)}, next_address: {id(current_node.next)} \n", end=" -> ")
start_node = n5
current_node = current_node.previous

while current_node != start_node:
    if current_node.previous:
        print(f"data: {current_node.data}, address: {id(current_node)}, prev_address: {
              id(current_node.previous)} \n", end=" -> ")
    else:
        print(f"data: {current_node.data}, address: {
              id(current_node)}, prev_address : None")
    current_node = current_node.previous