import numpy as np

class Stack:
    def __init__(self,arr,top = -1):
        self.size = len(arr)
        self.top = len(arr) - 1

def isEmpty(st):
    if st.top == -1:
        return True
    else:
        return False

def isFull(st):
    if st.top == st.size - 1:
        return True
    else:
        return False

def push(st,k):
    if isFull(st):
        print("Stack is full")
    else:
        st.top += 1
        arr[st.top] = k

def size(st):
    if isEmpty(st):
        return 0
    elif isFull(st):
        return st.size
    else:
        return st.top + 1

def pop(st):
    if isEmpty(st):
        print("Stack is empty")
    else:
        st.top -= 1
        return (arr[st.top+1])    

def peek(st):
    if isEmpty(st):
        print("Stack is empty")
    else:
        return (arr[st.top]) 

if __name__ == '__main__':
    arr = np.array([10,20,30])
    st = Stack(arr)
    print(arr)
    print(pop(st))
    push(st,10)
    print(arr)
    print(peek(st))
    pop(st)
    print(size(st))
    push(st,100)
    print(size(st))