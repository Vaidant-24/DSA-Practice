# ReArrange LL in Odd/Even :-

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

def display(head):
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next
    print()

def ReArrangeLL(head):
    first = head
    sec = head.next
    ls = list()
    while first:
        ls.append(first.data)
        first = first.next
        if first:
            first = first.next
    while sec:
        ls.append(sec.data)
        sec = sec.next
        if sec:
            sec = sec.next
    temp = head
    i = 0
    while temp and i<len(ls):
        temp.data = ls[i]
        temp = temp.next
        i += 1
    return head

def OptimalreArrangeLL(head):
    odd = head
    even = head.next
    evenHead = even
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next
    odd.next = evenHead
    return head
# head = ReArrangeLL(head)
display(head)
head = OptimalreArrangeLL(head)
display(head)