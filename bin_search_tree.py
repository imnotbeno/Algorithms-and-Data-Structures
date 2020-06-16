# !python3

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.key = key 

def search(root,key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None or root.key == key: 
        return root 
  
    # Key is greater than root's key 
    if root.key < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key)   

# Inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.key) 
        inorder(root.right) 
   
# Node insert function 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.key < node.key: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 

# Function to find inorder successor
def minValNode(node):
    current = node

    while current.key is not None:
        current = current.left 
    return current 
    
# Deleting a node in the tree
def delete(root, key):
    
    if root is None:
        return None

    if key < root.key:
        root.left = delete(root.left, key)
    
    elif key > root.key:
        root.right = delete(root.right, key)

    else:

        # Node with only one or no child
        if root.left is None:
            tmp = root.right
            root = None
            return tmp
        
        if root.right is None:
            tmp = root.left
            root = None 
            return tmp

        # Getting the inorder successor
        tmp = minValNode(root.right)

        # Copying the inorder succesor's key to root key
        root.key = tmp.key

        # Delete the inorder successor
        root.right = delete(root.right, tmp.key)
    
    return root
  
# Driver program to test the above functions 
# Let us create the following BST 
#      50 
#    /      \ 
#   30     70 
#   / \    / \ 
#  20 40  60 80 
r = Node(50) 
insert(r,Node(30)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80)) 
  
# Print inoder traversal of the BST 
print("Before deleting a node")
inorder(r) 

print("After deleting a leaf")
delete(r, 20)
inorder(r)

print("After deleting a leaf")
delete(r, 50)
inorder(r)

# print("After deleting a node with 2 child nodes")
# delete(r, 30)
# inorder(r)

# Worst case time complexity of both search
# and insert is O(h) where h is the height 
# of the tree