# Sort LL:-
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
    slow = fast = head
    fast = fast.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeLL(head1,head2):
    dummy = Node(-1)
    t1 = head1
    t2 = head2
    temp = dummy
    while t1 and t2:
        if t1.data < t2.data:
            temp.next = t1
            temp = t1
            t1 = t1.next
        else:
            temp.next = t2
            temp = t2
            t2 = t2.next
    if t1:
        temp.next = t1
    else:
        temp.next = t2
    head = dummy.next
    return head

def sortLL(head):
    temp = temp1 = head 
       
    while temp1.next:
        temp = head
        while temp.next:
            if temp.data > temp.next.data:
                temp.data,temp.next.data = temp.next.data,temp.data
            temp = temp.next
        temp1 = temp1.next
    return head

def mergeSortLL(head):
    if not head or not head.next:
        return head
    
    middle = middleOfLL(head)
    leftHead = head  
    rightHead = middle.next
    middle.next = None    
    leftSorted = mergeSortLL(leftHead)
    rightSorted = mergeSortLL(rightHead)
    return mergeLL(leftSorted,rightSorted)

head = Node(4)
head.next = Node(3)
head.next.next = Node(6)
head.next.next.next = Node(1)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next = Node(2)

head = mergeSortLL(head)
display(head)