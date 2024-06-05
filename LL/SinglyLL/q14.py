# Add 1 to a number represented by LL :-
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

def lengthOfLL(head):
    cnt = 0
    mov = head
    while mov:
        cnt += 1
        mov = mov.next
    return cnt

head = Node(1)
head.next = Node(5)
head.next.next = Node(9)


def ReverseLL(head):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def add1ToLL(head):
    newHead = ReverseLL(head)
    carry = 0
    temp = newHead
    sum = 0
    dummy = Node(-1)
    curr = dummy
    while temp:
        if temp == newHead:
            sum = carry + temp.data + 1
            carry = 1 if sum >= 10 else 0
            temp = temp.next
            newNode = Node(sum % 10)
            curr.next = newNode
            curr = curr.next
        else:    
            sum = carry + temp.data + 0
            carry = 1 if sum >= 10 else 0
            temp = temp.next
            newNode = Node(sum % 10)
            curr.next = newNode
            curr = curr.next
 
    if carry == 1:
        sum = carry
        newNode = Node(sum % 10)
        curr.next = newNode
        curr = curr.next

    return ReverseLL(dummy.next)

def helper(head):
    temp = head
    if not temp:
        return 1
    carry = helper(temp.next)
    temp.data += carry
    if temp.data < 10:
        return 0
    temp.data = 0
    return 1

def add1toLLRecursion(head):
    carry = helper(head)
    if carry == 1:
        newNode = Node(1)
        newNode.next = head
        head = newNode
    return head

display(head)
# newhead = add1ToLL(head)
# display(newhead)
new = add1toLLRecursion(head)
display(new)