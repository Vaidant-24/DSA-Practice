# Merge two sorted LL:-

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

def convertArr2LL(arr):           # Create a LL using array
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    
    return head


arr1 = [1,4,5,9,12]
arr2 = [2,3,6,8,10,11,13,18,20]


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

head1 = convertArr2LL(arr1)
head2 = convertArr2LL(arr2)
display(head1)
display(head2)
head = mergeLL(head1,head2)
display(head)