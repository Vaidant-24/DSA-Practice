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
root.left.left.left = Node(70)
root.left.left.right = Node(80)
root.left.right.right = Node(90)
root.right.left = Node(60)


def inIterative(root):
    curr = root
    st = []
    if not curr: return
    while curr:
        st.append(curr)
        curr = curr.left
    while len(st) > 0:
        temp = st.pop()
        print(temp.key)
        temp = temp.right
        while temp:
            st.append(temp)
            temp = temp.left

print(inIterative(root))