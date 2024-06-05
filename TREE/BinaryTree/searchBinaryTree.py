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
root.right.right = Node(11)

def searchKey(root,val):
    if root == None:
        return False
    else:
        if val == root.key:
            return True
        
        ls = searchKey(root.left,val)
        rs = searchKey(root.right,val)
        return ls or rs
    
print(searchKey(root,11))