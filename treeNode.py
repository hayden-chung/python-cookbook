class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def insert(root, key):
    if root is None: 
        return Node(key)
    
    if key < root.val:
        root.left = insert(root.left, key)
    
    if key > root.val: 
        root.right = insert(root.right, key)

    return root 

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

r = Node (50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

inorder_traversal(r)
        
