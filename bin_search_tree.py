# !python3

class Node:

    def __init__(self, key):
        self.key = key 
        self.left = None
        self.right = None


# Search function
def search(root, val):

    if root is None or root.key == val:
        return root

    if root.key < val:
        return search(root.right, val)
        
    if root.key > val:
        return search(root.left, val) 

# Insertion function
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.key < node.key:
            if root.right == None:
                root.right = node 
            else: 
                insert(root, node)

        if root.key > node.key:
            if root.left == None:
                root.left = node 
            else: 
                insert(root, node)

# Inorder traversal/print function
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
    

# Driver code
if __name__ == "__main__":

    root = Node(6)
    root.right = Node(10)
    root.left = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(1)
    root.right.right = Node(12)
    root.right.left = Node(8)

    search(root, 10)
    

