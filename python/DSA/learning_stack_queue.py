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

# OOP -> demo

# class Car:
#     def __init__(self, color, model, car_name):
#         self.color = color
#         self.model = model
#         self.car_name = car_name
#         self.speed = 0
#
#     def start(self):
#         return f"{self.color} color {self.model} model {self.car_name} is starting..."
#
#     def a(self, speed):
#         self.speed += speed
#         return self.speed
#
# bmw_color = "Blue"
# bmw_model = "A1"
# bmw_car_name = "BMW"
#
# BMW = Car(bmw_color, bmw_model, bmw_car_name)
# print(BMW.color)
# print(BMW.model)
# print(BMW.start())
# print(BMW.a(60))

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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size


myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
