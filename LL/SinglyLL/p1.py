class Node:
    def __init__(self,data1,next1 = None):
        self.data = data1
        self.next = next1

def convertArr2LL(arr):           # Create a LL using array
    head = Node(arr[0])
    mover = head
    for i in range(1,len(arr)):
        temp = Node(arr[i])
        mover.next = temp
        mover = temp
    
    return head

def displayLL(head):
    mv = head
    while mv:
        print(mv.data,end= ' ')
        mv = mv.next
    print()

def lengthOfLL(head):
    cnt = 0
    mov = head
    while mov:
        cnt += 1
        mov = mov.next
    
    return cnt

def searchLL(head,k):
    mov = head
    while mov:
        if mov.data == k:
            return True
        mov = mov.next
    return False

def insertFirstInLL(head,k):
    temp = Node(k)
    temp.next = head
    head = temp
    return head

def insertLastInLL(head,k):
    temp = head
    while temp.next:
        temp = temp.next
    new = Node(k)
    temp.next = new
    return head


def InsertNodeInLL(head,pos,k):
    p = head
    if pos == 0:
        temp = Node(k)
        temp.next = head
        head = temp
        return head

    for i in range(pos-1):
        p = p.next
    temp = Node(k)
    temp.next = p.next
    p.next = temp
    return head

def deleteTailOfLL(head):
    if head is None or head.next is None:  # If LL is empty or only one element
        return None
    
    temp = head
    prev = None
    while temp.next is not None:
        prev = temp 
        temp = temp.next

    prev.next = None
    return head

def deleteNodeInLL(head,node):
    temp = head
    if temp.data == node:       # When node to be deleted is first node
        head = temp.next
        temp.next = None
        return head
    
    prev = None
    while temp.data != node and temp is not None:
        prev = temp
        temp = temp.next
    if temp is not None:
        prev.next = temp.next
    else:
        prev.next = None
    return head

def ReverseLL(head):
    curr = head
    prev = None
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
arr = [2,3,1,4,5]
head = convertArr2LL(arr)
# head = deleteTailOfLL(head)
# displayLL(head)
# head = deleteNodeInLL(head,2)
# displayLL(head)
# head = InsertNodeInLL(head,2,10)
# displayLL(head)
# head = InsertNodeInLL(head,0,8)
displayLL(head)
head = ReverseLL(head)
displayLL(head)