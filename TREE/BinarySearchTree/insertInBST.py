class Node:
    def __init__(self,key):
        self.left = None
        self.key = key
        self.right = None

root = Node(50)
root.left = Node(40)
root.right = Node(60)
root.left.left = Node(30)
root.left.right = Node(45)
root.right.right = Node(70)


def recInsertBST(root,key):
    if root == None:
        return Node(key)
    
    if root.key == key:
        return root

    elif key < root.key:
        root.left = recInsertBST(root.left,key)
    
    elif key > root.key:
        root.right = recInsertBST(root.right,key) 
    
    return root

def insertBST(root,key):
    if root == None:
        return Node(key)
    
    while root:
        prev = root
        if key == root.key:
            return root
        elif key < root.key:
            root = root.left
        elif key > root.key:
            root = root.right

    if key < prev.key:
        new = Node(key)
        prev.left = new
    elif key > prev.key:
        new = Node(key)
        prev.right = new

insertBST(root,4)
insertBST(root,35)
insertBST(root,100)
insertBST(root,100)

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.key)
        inOrder(root.right)


recInsertBST(root,1)
recInsertBST(root,50)
recInsertBST(root,66)
recInsertBST(root,200)

print(inOrder(root))