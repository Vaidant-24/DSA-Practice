def floorBST(root,key):
    maxi = float('-inf')
    if root == None and maxi != float('-inf'): return maxi
    
    if key == root.key:
        return key
    elif key < root.key:
        floorBST(root.left,key)
    elif key > root.key:
        maxi = max(maxi, root.key)
        floorBST(root.right,key)
        
def IterativeFloorBST(root,key):
    res = None
    if root == None:
        return None
    
    while root:
        if key == root.key:
            return root
        elif key < root.key:
            root = root.left
        elif key > root.key:
            res = root
            root = root.right
    return res
            