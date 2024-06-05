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

def preOrder(root):
    if root != None:
        print(root.key)
        preOrder(root.left)
        preOrder(root.right)
        
print(preOrder(root))