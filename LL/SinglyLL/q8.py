# Remove middle node from the LL:-

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

def len(head):
    temp = head
    cnt = 0
    while temp:
        cnt += 1
        temp = temp.next
    return cnt

def display(head):
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next
    print()

def removeMiddleFromLL(head):
    n = len(head)
    if n == 0 or n == 1:
        return None
    res = n//2 
    temp = head
    while res != 0:
        res -= 1
        if res == 0:
            break
    temp = temp.next
    if temp:
        temp.next = temp.next.next
    return head

def removeMiddleFromLLOptimal(head):
    if head is None or head.next is None:
        return None
    slow = fast = head
    fast = fast.next.next
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    slow.next = slow.next.next
    return head
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)

head = removeMiddleFromLL(head)
display(head)