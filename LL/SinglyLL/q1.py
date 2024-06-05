# return middle of Linked List:-

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None
def display(head):
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next
    print()

def middleOfLL(head):
    cnt = 0
    temp = head
    while temp:
        cnt += 1
        temp = temp.next
    if cnt == 0 or cnt == 1:
        return None
    mid = (cnt//2) + 1
    temp = head
    for i in range(1,mid):
        temp = temp.next
    return temp

def middleOfLLOptimal(head):
    temp = head
    cnt = 1
    m = 1
    prev = 1
    mid = head
    while temp.next:
        cnt += 1
        prev = m
        m = (cnt//2) + 1
        if prev != m:
            mid = mid.next
        temp = temp.next
    return mid

def middleOfLL(head):
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

head = Node(1)
head.next = Node(2)

head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
# head.next.next.next.next.next = Node(6)
display(head)
mid = middleOfLL(head)
display(mid)
mid = middleOfLLOptimal(head)
display(mid)
mid = middleOfLL(head)
display(mid)