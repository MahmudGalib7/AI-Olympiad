"""
tree -> non-linear dsa
node -> element
edge -> link between parent and children
leaf -> node with no children
parent-child -> node connected downwards, here upward is parent and the downward one is child
subtree -> smaller tree linked with the main tree/ nested tree

tree:
1) first node/ head node is called root which can also be called parent
2) and other node derives from the root called children
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, child):
        self.children.append(child)

    def printTree(self, currentNode=0):
        print(' ' * currentNode * 4 + str(self.data))
        for child in self.children:
            child.printTree(currentNode + 1)

# Build a tree
root = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

root.addChild(b)
b.addChild(c)
b.addChild(d)
c.addChild(e)

root.printTree()