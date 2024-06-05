class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
        
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
        
    def enqueue(self, data):
        node = Node(data)
        if self.rear is None:
            self.front = node
        else:
            self.rear.next = node
        self.rear = node
        self.size += 1
        
    def dequeue(self):
        if self.front is None:
            return "Queue is empty"
        else:
            temp = self.front
            res = temp.data
            self.front = self.front.next
            
            if self.front is None:
                self.rear = None
                
            temp.next = None
            self.size -= 1
            return res
        
    def is_empty(self):
        return self.size == 0
    
    def get_front(self):
        if self.front is None:
            return "Queue is empty"
        return self.front.data

    def get_rear(self):
        if self.rear is None:
            return "Queue is empty"
        return self.rear.data
        
    def display(self):
        temp = self.front
        while temp:
            print(temp.data,end=' ')
            temp = temp.next
        print("\n")
            
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.get_rear())

q.enqueue(40)

print(q.get_rear())

q.display()

print(q.get_front())

print(q.dequeue())

print(q.get_front())

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.is_empty())
print(q.get_front())
print(q.get_rear())