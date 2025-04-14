class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def del_node(head, del_node):
    if del_node == head:
        return head.next
    current_node = head
    while current_node.next and current_node.next != del_node:
        current_node = current_node.next
    if current_node.next is None:
        return head
    current_node.next = current_node.next.next
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

print("\nBefore deletion:")
traverse_and_print(n1)

head = del_node(n1, n3)

print("\nAfter deletion:")
traverse_and_print(n1)