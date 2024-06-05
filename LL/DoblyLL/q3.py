# Find pair with given sum k:-
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

def pairOfSum(head,k):
    first = head
    temp = head
    ls = list()
    while temp.next:
        temp = temp.next
    last = temp

    while first.data < last.data:
        if (first.data + last.data) == k:
            tempList = [first.data, last.data]
            first = first.next
            last = last.prev
            ls.append(tempList)
        elif (first.data + last.data) > k:
            last = last.prev
        else:
            first = first.next
    return ls

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,9]
    head = arr2DLL(arr)
    displayDLL(head)
    print(pairOfSum(head,8))
