class Node:
    def __init__(self,key):
        self.left = None
        self.key = key
        self.right = None
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.key)
        inOrder(root.right)
        
print(inOrder(root))