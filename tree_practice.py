class Node:
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < r.v:
        root.left = insert(root.left, val)
    if val > r.v:
        root.right = insert(root.right, val)

    return root

def get_max_length(root):
    

def traversal(root, length):
    length += 1
    if root:
        traversal(root.left, length)
        print(root.v)
        traversal(root.right, length)

r = Node(50)
r = insert(r, 30)
r = insert(r, 100)
# r = insert(r, 55)
# r = insert(r, 70)
# r = insert(r, 1)

traversal(r, 0)