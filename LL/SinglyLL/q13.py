# Find sum of 2LL:-
class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = None

def insertLastInLL(head,k):
    temp = head
    while temp.next:
        temp = temp.next
    new = Node(k)
    temp.next = new

def display(head):
    temp = head
    while temp:
        print(temp.val,end=' ')
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
def sum_2LL(headA,headB):
    t1 = headA
    t2 = headB
    carry = 0
    dummy = Node(-1)
    curr = dummy
    while t1 and t2:
        sum = t1.val + t2.val + carry
        carry = 1 if sum >= 10 else 0
        rem = sum % 10
        new = Node(rem)
        curr.next = new
        curr = curr.next
        t1 = t1.next
        t2 = t2.next

    while t1:
        sum = t1.val + carry
        carry = 1 if sum >= 10 else 0
        rem = sum % 10
        new = Node(rem)
        curr.next = new
        curr = curr.next
        t1 = t1.next
    while t2:
        sum = t2.val + carry
        carry = 1 if sum >= 10 else 0
        rem = sum % 10
        new = Node(rem)
        curr.next = new
        curr = curr.next
        t2 = t2.next
    if t1 is None and t2 is None:
        if carry == 1:
            sum = carry 
            rem = sum % 10
            new = Node(rem)
            curr.next = new
            curr = curr.next
    return dummy.next

arr1 = [1,4,9,8]
arr2 = [2,9,4]
head1 = convertArr2LL(arr1)
head2 = convertArr2LL(arr2)
head = sum_2LL(head1, head2)
display(head)