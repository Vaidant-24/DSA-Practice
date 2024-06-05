# Find if LL is pallindrome or not:-
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

def isPallindrome(head):
    lst = []
    temp = head
    while temp:
        lst.append(temp.data)
        temp = temp.next
    flag = 0
    temp = head
    for i in range(len(lst)-1,-1,-1):
        if temp.data == lst[i]:
            temp = temp.next
        else:
            flag = 1
            break

    if flag == 1:
        return False
    else: 
        return True

# Using stack:-
from collections import deque
def isPallindromeDeQueue(head):
    st = deque()
    temp = head
    while temp:
        st.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        if temp.data != st.pop():
            return False
        temp = temp.next
    return True

# Optimal Solution using reverse function:-
def ReverseLL(head):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head = prev
    return head

def isPallindromeOptimal(head):
    slow = fast = temp1 = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow
    
    temp2 = ReverseLL(mid.next)
    while temp1 != mid.next and temp2 != None:
        if temp1.data != temp2.data:
            return False
        temp1 = temp1.next
        temp2 = temp2.next
    return True

def display(head):
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next
    print()

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)
# head.next.next.next.next.next = Node(1)


print(isPallindrome(head))
print(isPallindromeDeQueue(head))
print(isPallindromeOptimal(head))
mid = isPallindromeOptimal(head)
display(mid)