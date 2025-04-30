# Example refactoring based on your files
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Based on inserting_nodes_in_linked_list.py
    def insert_at_position(self, data, pos):
        new_node = Node(data)
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        current_node = self.head
        # Need to handle case where head is None if pos > 1
        if not current_node and pos > 1:
             print(f"Cannot insert at position {pos} in empty list")
             return
        # Iterate pos-2 times to get to the node *before* insertion point
        for _ in range(pos - 2):
            if current_node and current_node.next: # Check if next exists
                current_node = current_node.next
            else:
                # Position is out of bounds or at the very end
                print(f"Position {pos} is out of bounds or list is too short.")
                # Decide if you want to append or return error
                # If append: find last node and append new_node
                # If error: return
                return # Example: return error

        # Check if current_node is valid after loop
        if not current_node:
             print(f"Position {pos} seems invalid.")
             return

        new_node.next = current_node.next
        current_node.next = new_node

    # Based on deleting_node_from_linked_list.py (modified to delete by value)
    def delete_node_by_value(self, key):
        temp = self.head
        # If head node itself holds the key
        if temp and temp.data == key:
            self.head = temp.next
            return
        # Search for the key, keeping track of the previous node
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        # If key was not present
        if not temp:
            print(f"Value {key} not found.")
            return
        # Unlink the node
        prev.next = temp.next

    # Based on min_value_from_linked_list.py
    def find_min_value(self):
        if not self.head:
            return None # Handle empty list

        min_value = self.head.data
        current_node = self.head.next
        while current_node:
            if current_node.data < min_value:
                min_value = current_node.data
            current_node = current_node.next
        return min_value

    # Based on traverse_and_print
    def print_list(self):
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        print(" -> ".join(nodes) + " -> None")

# Usage:
my_list = LinkedList()
my_list.insert_at_position(10, 1)
my_list.insert_at_position(20, 2)
my_list.insert_at_position(15, 2)
my_list.print_list() # Output: 10 -> 15 -> 20 -> None
print(my_list.find_min_value()) # Output: 10
my_list.delete_node_by_value(15)
my_list.print_list() # Output: 10 -> 20 -> None