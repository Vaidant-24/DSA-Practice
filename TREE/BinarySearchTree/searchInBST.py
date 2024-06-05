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


def search(root,key):
    while root:
        if root.key == key: return True
        elif key < root.key:
            root = root.left
        elif key > root.key:
            root = root.right
    return False

def recSearch(root,key):
    if root is None: return False
    
    elif root.key == key: return True
    elif key < root.key:
        recSearch(root.left,key)
    elif key > root.key:
        recSearch(root.right,key)

print(search(root,70))
print(search(root,70))