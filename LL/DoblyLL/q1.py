# Delete all occurrences of a key in DLL:-
class Node:
    def __init__(self,val,next = None,back = None):
        self.val = val
        self.next = next
        self.back = back

def displayDLL(head):
    while head:
        print(head.val,end=' ')
        head = head.next
    print()

def arr2DLL(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp
    
    return head

def deleteAllOccurences(head,k):
    if not head:
       return None
    if not head.next:
        if head.val == k:
            return None
        else:
            return head
    temp = head
    while temp:
        if temp.val == k:
            if temp == head:
                head = temp.next
            prevNode = temp.back
            nextNode = temp.next
            if nextNode: nextNode.back = prevNode
            if prevNode: prevNode.next = nextNode
            temp = nextNode
        else:
            temp = temp.next 
    return head

if __name__ == '__main__':
    arr = [10,10]
    head = arr2DLL(arr)
    displayDLL(head)
    newHead = deleteAllOccurences(head,10)
    displayDLL(newHead)