class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.key = data


# Function to insert element into binary tree
def insert(key, node):

    q = []
    q.append(node)

    # Do level order traversal until
    # we find an empty place
    while len(q):
        node = q[0]
        q.pop(0)

        if not node.left:
            node.left = Node(key)
            break
        else:
            q.append(node.left)

        if not node.right:
            node.right = Node(key)
            break
        else:
            q.append(node.right)

# Function to find and delete the deepest right node in a binary tree
def deleteDeepest(root, d_node):
    q = []
    q.append(root)

    while len(q):
        r_temp = q.pop(0)
        
        if r_temp is d_node:
            r_temp = None 
            return 

        if r_temp.right:
            if r_temp.right is d_node:
                r_temp.right = None 
                return
            else: 
                q.append(r_temp.right)
                
        if r_temp.left:
            if r_temp.left is d_node:
                r_temp.left = None 
                return
            else: 
                q.append(r_temp.left)

# Function to delete binary tree element
def delete(key, node):

    if node == None:
        return None
    if node.left == None and node.right == None:
        if node.key == key:
            return None
        else: 
            return node
    
    key_node = None 
    q = []
    q.append(node)

    while len(q):
        r_temp = q.pop(0) 
        
        if r_temp.key == key:
            key_node = r_temp

        if r_temp.left:
            q.append(r_temp.left)
            
        if r_temp.right:
            q.append(r_temp.right)

    if key_node: 
        x = r_temp.key
        deleteDeepest(node, r_temp)
        key_node.key = x
    return node 

# Tree traversal inorder(left, root, right)
def printInorder(node):
    if not node:
        return

    printInorder(node.left)
    print(node.key, end=" ")
    printInorder(node.right)


# Tree traversal preorder(root, left, right)
def printPreorder(node):

    if not node:
        return

    print(node.key, end=" ")
    printPreorder(node.left)
    printPreorder(node.right)


# Tree traversal postorder(left, right, root)
def printPostorder(node):

    if not node:
        return

    printPostorder(node.left)
    printPostorder(node.right)
    print(node.key, end=" ")


# Driver code
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.right = Node(9)
    root.right.right = Node(8)
    root.right.left = Node(15)

    print("Tree before deletion: ")
    printInorder(root)
    print("\nTree after deletion: ")
    dt = delete(11, root)
    printInorder(dt)

    # print("Inorder printing before insert: ", end=" ")
    # printInorder(root)
    #
    # key = 12
    # insert(key, root)
    #
    # print("\nInorder printing after insertion: ", end=" ")
    # printInorder(root)
    #
    # print("\nPreorder printing after insertion", end=" ")
    # printPreorder(root)
