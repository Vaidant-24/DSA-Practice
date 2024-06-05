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

def sortLLof012(head):
    if head is None or head.next is None:
        return head
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    mov = head
    while mov:
        if mov.data == 0:
            cnt0 += 1
        elif mov.data == 1:
            cnt1 += 1
        else:
            cnt2 += 1
        mov = mov.next
    len = cnt0 + cnt1 + cnt2
    temp = head
    for i in range(len):
        if cnt0 != 0:
            temp.data = 0
            cnt0 -= 1
        elif cnt1 != 0:
            temp.data = 1
            cnt1 -= 1
        elif cnt2 != 0:
            temp.data = 2
            cnt2 -= 1
        temp = temp.next
    return head

def sortLLOptimal012(head):
    if not head or not head.next:
        return head 
    temp = head
    L0 = Node(-1)
    L1 = Node(-1)
    L2 = Node(-1)
    lo = L0
    l1 = L1
    l2 = L2
    while temp:
        if temp.data == 0:
            lo.next = temp
            lo = temp
        elif temp.data == 1:
            l1.next = temp
            l1 = temp
        else:
            l2.next = temp
            l2 = temp
        temp = temp.next
    if L1.next:
        lo.next = L1.next
    else:
        lo.next = L2.next
    l1.next = L2.next
    l2.next = None
    Newhead = L0.next
    return Newhead
head = Node(0)
head.next = Node(0)
head.next.next = Node(0)
head.next.next.next = Node(0)
head.next.next.next.next = Node(1)


display(head)
new = sortLLof012(head)
display(new)
new2 = sortLLOptimal012(head)
display(new2)