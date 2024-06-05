class Node:
    def __init__(self,key):
        self.left = None
        self.key = key
        self.right = None
        
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(8)
root.left.right.left = Node(7)
root.right.right = Node(11)

def countHeight(root):
    if root == None:
        return 0
    
    ls = countHeight(root.left)
    rs = countHeight(root.right)
    return max(ls, rs) + 1

print(countHeight(root)) 