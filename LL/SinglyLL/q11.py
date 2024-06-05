# Find intersection Node in LL:-

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

head = Node(1)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)

head1 = Node(3)
head1.next = Node(4)
head1.next.next = head.next.next.next

# head1.next.next.next = Node(4)
# head1.next.next.next.next = Node(5)

def intersection_node(head1,head2):
    t1 = head1
    t2 = head2
    st = set()
    while t1:
        if t1 in st:
            return t1.data
        else:
            st.add(t1)
        t1 = t1.next
    while t2:
        if t2 in st:
            return t2.data
        else:
            st.add(t2)
        t2 = t2.next            
    return None

def lengthOfLL(head):
    cnt = 0
    mov = head
    while mov:
        cnt += 1
        mov = mov.next
    return cnt

def insersectionNode(head1, head2):
    t1 = head1
    t2 = head2
    l1 = lengthOfLL(t1)
    l2 = lengthOfLL(t2)
    diff = abs(l1 - l2)
    if l1 > l2:
        for i in range(diff):
            t1 = t1.next
    else:
        for i in range(diff):
            t2 = t2.next
    while t1 and t2:
        if t1 == t2: 
            return t1.data
        t1 = t1.next
        t2 = t2.next
    return None
print(intersection_node(head,head1))
print(insersectionNode(head,head1))