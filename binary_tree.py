# !python3
# Binary tree

class Node:

    def __init__(self, data):
        self.key = data
        self.right = None #They're set to None because we need to add nodes to the tree
        self.left = None

def printInorder(node):

    if node:
        printInorder(node.left)
        print(node.key)
        printInorder(node.right)

# Driver code
if __name__ == "__main__":
    root = Node(1)
    root.right = Node(3)
    root.left = Node(2)

    printInorder(root)
