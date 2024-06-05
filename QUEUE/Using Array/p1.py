class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.size = 10

def push(st,k):
    if st.rear == st.size - 1:
        print("Queue is full")
    
        