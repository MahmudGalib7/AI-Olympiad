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

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if self.is_empty():
            return f"stack is empty"
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return f"stack is empty"
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)
