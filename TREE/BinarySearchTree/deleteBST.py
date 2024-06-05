def getSuccessor(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr.key    

def delNode(root,key):
    if root == None: return
    
    if key < root.key:
        root.left = delNode(root.left,key)
    elif key > root.key:
        delNode(root.right,key)
        root.right = delNode(root.right,key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getSuccessor(root.right)
            root.key = succ
            root.right = delNode(root.right,succ)
    return root            
                   
     