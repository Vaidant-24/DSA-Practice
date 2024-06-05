# Find starting node of LL:-

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None


def locateLoopInLL(head):
    st = set()
    temp = head
    while temp:
        if temp in st:
            return temp.data
        st.add(temp)
        temp = temp.next
    return None

def locateLoopInLLOptimal(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        entry = head
        if slow == fast:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            return entry.data
    return None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next.next = head.next.next

print(locateLoopInLLOptimal(head))
