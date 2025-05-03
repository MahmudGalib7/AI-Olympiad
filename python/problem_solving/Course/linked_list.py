class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_linked_list(list1, list2):
    # Create a dummy node to act as a placeholder head
    dummy = Node(0) # The value 0 is arbitrary
    # 'node' will be the pointer to build the new list
    node = dummy

    # Loop while both lists have nodes
    while list1 and list2:
        if list1.data < list2.data:
            # Append list1's node
            node.next = list1
            # Move list1 pointer forward
            list1 = list1.next
        else:
            # Append list2's node
            node.next = list2
            # Move list2 pointer forward
            list2 = list2.next
        # Move the builder pointer forward
        node = node.next

    # Append the remaining nodes from whichever list is not empty
    node.next = list1 if list1 else list2

    # The merged list starts *after* the dummy node
    return dummy.next

# Helper function to print a linked list
def print_list(head):
    nodes = []
    current = head
    while current:
        nodes.append(str(current.data))
        current = current.next
    print(" -> ".join(nodes) + " -> None")

# --- Example 1 ---
print("Example 1:")
# list1: 1 -> 2 -> 4
l1_node1 = Node(1)
l1_node2 = Node(2)
l1_node3 = Node(4)
l1_node1.next = l1_node2
l1_node2.next = l1_node3
print("List 1:", end=" ")
print_list(l1_node1)

# list2: 1 -> 3 -> 4
l2_node1 = Node(1)
l2_node2 = Node(3)
l2_node3 = Node(4)
l2_node1.next = l2_node2
l2_node2.next = l2_node3
print("List 2:", end=" ")
print_list(l2_node1)

merged_head1 = merge_linked_list(l1_node1, l2_node1)
print("Merged:", end=" ")
print_list(merged_head1) # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> None
print("-" * 20)

# --- Example 2 ---
print("Example 2:")
# list1: None
l3_head = None
print("List 1:", end=" ")
print_list(l3_head)

# list2: 0
l4_node1 = Node(0)
print("List 2:", end=" ")
print_list(l4_node1)

merged_head2 = merge_linked_list(l3_head, l4_node1)
print("Merged:", end=" ")
print_list(merged_head2) # Expected: 0 -> None
print("-" * 20)

# --- Example 3 ---
print("Example 3:")
# list1: 2
l5_node1 = Node(2)
print("List 1:", end=" ")
print_list(l5_node1)

# list2: 1
l6_node1 = Node(1)
print("List 2:", end=" ")
print_list(l6_node1)

merged_head3 = merge_linked_list(l5_node1, l6_node1)
print("Merged:", end=" ")
print_list(merged_head3) # Expected: 1 -> 2 -> None
print("-" * 20)