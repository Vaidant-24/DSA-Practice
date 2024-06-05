# Remove nth node from end of LL:-
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = None


head = Node(1)
head.next = Node(2)
# head.next.next = Node(3)
# head.next.next.next = Node(4)
# head.next.next.next.next = Node(5)


def display(head):
    temp = head
    while temp:
        print(temp.data,end=' ')
        temp = temp.next
    print()

def len(head):
    temp = head
    cnt = 0
    while temp:
        cnt += 1
        temp = temp.next
    return cnt

def remove_nth_node_from_end(head,n):
    diff = len(head) - n
    temp = head
    prev = None
    if diff == 0:
        res = head.next
        return res
    else:
        for i in range(diff):
            prev = temp
            temp = temp.next
        prev.next = temp.next
        return head    
    
def remove_nth_node_Optimal(head,n):
    slow = fast = head
    for i in range(n):
        fast = fast.next
    if fast is None:
        return head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head
# head = remove_nth_node_from_end(head,1)
# display(head)
head = remove_nth_node_Optimal(head,2)
display(head)