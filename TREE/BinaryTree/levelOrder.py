from collections import deque

class Node:
    def __init__(self,key):
        self.left = None
        self.key = key
        self.right = None
        
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.right = Node(60)
root.left.right.left = Node(70)
root.left.right.right = Node(80)


def levelOrder(root):
    if root is None:
        return 
    q = deque()
    q.append(root)
    while len(q) > 0:
        curr = q.pop()
        print(curr.key)
        if curr.left:
            q.appendleft(curr.left)
        if curr.right:
            q.appendleft(curr.right)
            
print(levelOrder(root))