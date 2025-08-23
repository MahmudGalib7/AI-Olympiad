"""
tree -> non-linear dsa
node -> element
edge -> link between parent and children
leaf -> node with no children
parent-child -> node connected downwards, here upward is parent and the downward one is child
subtree -> smaller tree linked with the main tree/ nested tree

Binary Search tree:

In Depth first search ( DFS ):
     => There are three ways:
        - Preorder traversal = root -> left -> right
        - Inorder traversal = left -> root -> right
        - Postorder traversal = left -> right -> root

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            elif data > node.data:
                node.right = self.insert(node.right, data)
        return node

    def preorder(self, node):
        if node:
            node.preorder(node.left)
            node.preorder(node.right)

    def inorder(self, node):
        if node:
            node.inorder(node.left)
            node.inorder(node.right)

    def postorder(self, node):
        if node:
            node.postorder(node.left)
            node.postorder(node.right)
    def printPreorder(self, level=0):
        print(" " * level * 4 + str(self.data))
        if self.left:
            self.left.printPreorder(level + 1)
        if self.right:
            self.right.printPreorder(level + 1)

    def printInorder(self, level=0):
        if self.left:
            self.left.printInorder(level + 1)
        print(" " * level * 4 + str(self.data))
        if self.right:
            self.right.printInorder(level + 1)

    def printPostorder(self, level=0):
        if self.left:
            self.left.printPostorder(level + 1)
        if self.right:
            self.right.printPostorder(level + 1)
        print(" " * level * 4 + str(self.data))

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    def search(self, node, target):
        if node is None:
            return None
        if node.data == target:
            return node
        elif node.data > target:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)


# Build a tree
root = Node(1)
b = Node(2)

root.insert(root, 2)
root.insert(root, 3)
b.insert(b, 4)
b.insert(b, 5)

# Call the traversal and printing functions
print("Preorder (Indented):")
root.printPreorder()
print("\nInorder (Indented):")
root.printInorder()
print("\nPostorder (Indented):")
root.printPostorder()

print("\nHeight of the tree:")
print(root.height(root))