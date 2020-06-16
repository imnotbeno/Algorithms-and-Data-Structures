# !python3

class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 

def search(root,key): 
      
    # Base Cases: root is null or key is present at root 
    if root is None or root.val == key: 
        return root 
  
    # Key is greater than root's key 
    if root.val < key: 
        return search(root.right,key) 
    
    # Key is smaller than root's key 
    return search(root.left,key)   

# Node insert function 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
# Inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 
  
  
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
inorder(r) 

# Worst case time complexity of both search
# and insert is O(h) where h is the height 
# of the tree