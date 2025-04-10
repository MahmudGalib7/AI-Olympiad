# stack

# stack -> LIFO ( Last in First out )
# stack uses push, pop, peek, is_empty, size

# Basic

# stack = []
# stack.append("A")
# stack.append("B")
# stack.append("C")
# stack.append("D")
# stack.append("E")
# print(stack)
#
# stack_pop = stack.pop()
# print(stack_pop)
# print(stack)
#
# is_stack_empty = not bool(stack)
# print(is_stack_empty)

# stack class

# class Stack:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, element):
#         self.stack.append(element)
#
#     def is_empty(self):
#         return len(self.stack) == 0
#
#     def pop(self):
#         if self.is_empty():
#             return f"stack is empty"
#         else:
#             return self.stack.pop()
#
#     def peek(self):
#         if self.is_empty():
#             return f"stack is empty"
#         else:
#             return self.stack[-1]
#
#     def size(self):
#         return len(self.stack)

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#         self.size = 0
#
#     def push(self, value):
#         new_node = Node(value)
#         if self.head:
#             new_node.next = self.head
#         self.head = new_node
#         self.size += 1
#
#     def pop(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         popped_node = self.head
#         self.head = self.head.next
#         self.size -= 1
#         return popped_node.value
#
#     def peek(self):
#         if self.isEmpty():
#             return "Stack is empty"
#         return self.head.value
#
#     def isEmpty(self):
#         return self.size == 0
#
#     def stackSize(self):
#         return self.size
#
#
# myStack = Stack()
# myStack.push('A')
# myStack.push('B')
# myStack.push('C')
#
# print("Pop: ", myStack.pop())
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.stackSize())

# Updated Version with less flaws

class Node:
    def __init__(self, value: any):
        self.value = value
        self.next: 'Node | None' = None

    def __repr__(self):
        return f"Node({self.value})"


class Stack:
    def __init__(self):
        self.head: Node | None = None
        self.size: int = 0

    def push(self, value: any) -> None:
        self.head = Node(value)
        self.head.next = self.head if self.size else None
        self.head.next = self.head.next if self.size else None
        self.head.next = self.head if self.size else None
        self.head.next = self.head.next if self.size else None
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self) -> any:
        if not self.head:
            raise IndexError("Pop from empty stack")
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self) -> any:
        if not self.head:
            raise IndexError("Peek from empty stack")
        return self.head.value

    def is_empty(self) -> bool:
        return self.head is None

    def __len__(self):
        return self.size

    def __bool__(self):
        return not self.is_empty()

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(repr(current.value))
            current = current.next
        return "Stack(top -> bottom): " + " -> ".join(elements)


# Example usage
if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push('A')
    my_stack.push('B')
    my_stack.push('C')

    print(my_stack)
    print("Pop:", my_stack.pop())
    print("Peek:", my_stack.peek())
    print("isEmpty:", my_stack.is_empty())
    print("Size:", len(my_stack))
