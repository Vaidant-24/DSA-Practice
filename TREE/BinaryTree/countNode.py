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

def countNode(root):

    if root != None:
        ls = countNode(root.left)
        rs = countNode(root.right)
        return ls + rs + 1
    
    if root == None:
        return 0
    

    
        

print(countNode(root))