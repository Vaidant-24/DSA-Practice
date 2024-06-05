# Find length of LL:-

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

def lenOfLoopInLL(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        entry = head
        cnt = 0
        if slow == fast:
            while slow != entry:
                slow = slow.next
                entry = entry.next
            cur = entry
            entry = entry.next
            while entry != cur:
                cnt += 1
                entry = entry.next
            return cnt 
    return None



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next.next = head.next.next

print(lenOfLoopInLL(head))