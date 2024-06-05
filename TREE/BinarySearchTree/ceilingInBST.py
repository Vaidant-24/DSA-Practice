def IterativeCeilingBST(root,key):
    res = None
    while root:
        if key == root.key:
            return root
        elif key < root.key:
            res = root
            root = root.left
        elif key > root.key:
            root = root.right
    return res            