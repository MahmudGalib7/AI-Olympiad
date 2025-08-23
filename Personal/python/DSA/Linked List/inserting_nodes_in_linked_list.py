class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insert_new_node(head, new_node, pos):
    if pos == 1:
        new_node.next = head
        return new_node

    current_node = head
    for i in range(pos - 2):
        if current_node:
            current_node = current_node.next
        else:
            break

    new_node.next = current_node.next
    current_node.next = new_node
    return head

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

print("\nBefore insertion:")
traverse_and_print(n1)

new_node = Node(350)
insert_new_node(n1, new_node, 2)

print("\nAfter insertion:")
traverse_and_print(n1)