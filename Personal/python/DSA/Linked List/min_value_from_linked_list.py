class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_lowest(head):
    min_value = head.data
    current_node = head.next
    while current_node:
        if current_node.data < min_value:
            min_value = current_node.data
        current_node = current_node.next
    return min_value

def traverse_and_print(head):
    current_node = head
    while current_node:
        if current_node.next:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        else:
            print(current_node.data)
            break

n1 = Node(150)
n2 = Node(1000)
n3 = Node(100)
n4 = Node(200)
n5 = Node(50)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

print(find_lowest(n1))