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
root.right.left = Node(60)
root.right.right = Node(80)


def preIterative1(root):
    
    if root == None: return
    curr = root
    st = []
    if not curr:
        return 
    while curr:
        print(curr.key)
        st.append(curr)
        curr = curr.left
    while len(st) > 0:
        temp = st.pop()
        temp = temp.right
        while temp:
            print(temp.key)
            st.append(temp)
            temp = temp.left

print(preIterative1(root))

def preIterative2(root):
    if root == None:
        return
    st = [root]
    while len(st) > 0:
        curr = st.pop()
        print(curr.key)
        if curr.right:
            st.append(curr.right)
        if curr.left:
            st.append(curr.left)
        
print(preIterative2(root))