class Queue:
    def __init__(self,capacity):
        self.front = 0
        self.size = 0
        self.cap = capacity
        self.ls = [None] * capacity
        
    def enqueue(self,val):
        if self.size == self.cap:
            return "Queue is full"
        rear = self.front + self.size - 1
        rear = (rear + 1) % self.cap
        self.ls[rear] = val
        self.size += 1
        
    def dequeue(self):
        if self.size == 0:
            return None
        val = self.ls[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return val
    
    def get_front(self):
        if self.size == 0:
            return None
        return self.ls[self.front]

    def get_rear(self):
        if self.size == 0:
            return None
        rear = self.front + self.size - 1
        return self.ls[rear]
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
q = Queue(4)
print(q.is_empty())
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
print(q.enqueue(8))
print(q.ls)
print(q.get_size())
print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.get_front())
print(q.get_rear())