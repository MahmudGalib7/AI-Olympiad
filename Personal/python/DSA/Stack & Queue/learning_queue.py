# Queue

# Queue -> FIFO ( First In First Out )
# stack uses Enqueue, Dequeue, Peek, isEmpty, Size

# Basic

# queue = []

# queue.append('A')
# queue.append('B')
# queue.append('C')
# print("Queue: ", queue)
#
# element = queue.pop(0)
# print(element)
# first_element = queue[0]
# print(first_element)
# isEmpty = not bool(queue)
# print("isEmpty: ", isEmpty)
# print(len(queue))

# Using OOP

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


queue = Queue()
queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
print("Queue: ", queue.queue)
print("Dequeue: ", queue.dequeue())
print("Peek: ", queue.peek())
print("isEmpty: ", queue.isEmpty())
print("Size: ", queue.size())
