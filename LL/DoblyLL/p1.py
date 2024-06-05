class Node:
    def __init__(self,data,next = None,back = None):
        self.data = data
        self.next = next
        self.back = back

def arr2DLL(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp
    
    return head

def deleteinDLL(head,pos):
    if head is None or head.next is None:
        return None
    
    p = head
    if pos == 1:
        head = head.next
        head.back = None
        p.next = None
        return head
    
    for i in range(pos-1):
        p = p.next

    prev = p.back
    p.back = None
    prev.next = p.next
    p.next = None
    
    return head

def deleteAtHeadInDLL(head):
    temp = head
    head = head.next
    head.back = None
    temp.next = None
    return head

def deleteAtTailInDLL(head):
    temp = head
    prev = None
    while temp.next is not None:
        prev = temp
        temp = temp.next
    temp.back = None
    prev.next = None
    return head

def insertAtHeadInDLL(head,data):
    temp = Node(data,head,None)
    head.back = temp
    head = temp
    return head

def insertAtTailInDLL(head,data):
    temp = head
    while temp.next is not None:
        temp = temp.next
    new = Node(data,None,temp)
    temp.next = new
    return head

def insertInDLL(head,data,pos):
    if pos == 1:
        temp = Node(data,head,None)
        head.back = temp
        head = temp
        return head
    else:
        p = head
        q = None
        for i in range(pos-1):
            q = p
            p = p.next 
        if p is None:
            temp = Node(data,None,q)
            q.next = temp
            return head
        else:
            temp = Node(data,p,q)  
            q.next = temp
            p.back = temp        
            return head
        
def displayDLL(head):
    while head:
        print(head.data,end=' ')
        head = head.next
    print()

def ReverseDLL(head):
    last = None
    curr = head
    while curr:
        last = curr.back
        curr.back = curr.next
        curr.next = last
        curr = curr.back
    head = last.back
    return head


arr = [2,3,1,5,8]
head = arr2DLL(arr)
# displayDLL(head)
# head = deleteinDLL(head,5)
# displayDLL(head)
# head = insertAtHeadInDLL(head,10)
# displayDLL(head)
# head = insertAtTailInDLL(head,100)
# displayDLL(head)
# head = deleteAtHeadInDLL(head)
# displayDLL(head)
# head = deleteAtTailInDLL(head)
# displayDLL(head)
# head = insertInDLL(head,100,6)
# displayDLL(head)
head = ReverseDLL(head)
displayDLL(head)