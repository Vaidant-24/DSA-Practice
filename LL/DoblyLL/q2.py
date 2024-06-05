# Remove Duplicates from sorted DLL:-
class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

def displayDLL(head):
    while head:
        print(head.data,end=' ')
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
def removeDuplicatesFromDll(head):
    if not head or not head.next:
        return head
    st = set()
    temp = head
    while temp:
        if temp.data not in st:
            st.add(temp.data)
            temp = temp.next
        else:
            prevNode = temp.prev
            nextNode = temp.next
            if nextNode: nextNode.prev = prevNode
            if prevNode: prevNode.next = nextNode
            temp = nextNode
    return head
def removeDuplicatesOptimal(head):
    if not head or not head.next:
        return head
    temp = head
    while temp and temp.next:
        nextNode = temp.next
        while nextNode and temp.data == nextNode.data:
            nextNode = nextNode.next
        temp.next = nextNode
        if nextNode: nextNode.prev = temp
        temp = nextNode
    return head

if __name__ == '__main__':
    arr = [1]
    head = arr2DLL(arr)
    displayDLL(head)
    # newHead = removeDuplicatesFromDll(head)
    # displayDLL(newHead)
    newHead = removeDuplicatesOptimal(head)
    displayDLL(newHead)