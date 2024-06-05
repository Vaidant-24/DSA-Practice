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
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(4)
head.next.next.next.next.next.next = Node(4)

