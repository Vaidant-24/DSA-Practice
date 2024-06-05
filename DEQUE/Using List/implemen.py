class Deque:
    def __init__(self,capacity) -> None:
        self.cap = capacity
        self.ls = [None] * capacity
        self.front = 0
        self.size = 0
        
    def insertRear(self,data):
        if self.size == self.cap:
            return "Deque is full"
        
        rear = self.front + self.size - 1
        rear = (rear + 1) % self.cap
        self.ls[rear] = data
        self.size += 1
        
    def deleteFront(self):
        if self.size == 0:
            return "Deque is empty"
        
        val = self.ls[self.front]
        self.front = (self.front + 1) % self.cap
        self.size -= 1
        return val
    
    def insertFront(self, data):
        if self.size == self.cap:
            return "Deque is full"
        self.front = (self.front - 1) % self.cap
        self.ls[self.front] = data
        self.size += 1
        
    def deleteRear(self):
        if self.size == 0:
            return "Deque is empty"
        rear = self.front + self.size - 1
        val = self.ls[rear]
        rear = (rear - 1) % self.cap
        self.size -= 1
        return val
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def getRear(self):
        if self.size == 0:
            return None
        return self.ls[self.rear]
    
    def getFront(self):
        if self.size == 0:
            return None
        return self.ls[self.front]    
        
d = Deque(5)
d.insertRear(10)
d.insertRear(20)
d.insertRear(30)
print(d.ls)
print(d.deleteFront())
print(d.deleteFront())
d.insertFront(50)
d.insertFront(60)
print(d.ls)
print(d.deleteRear())
print(d.deleteRear())
