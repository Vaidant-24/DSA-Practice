class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class Deque:
    def __init__(self):
        self.rear = None
        self.front = None
        self.size = 0
        
    def insertRear(self,val):
        new = Node(val)
        if self.rear is None:
            self.front = new
        else:
            self.rear.next = new
        new.prev = self.rear
        self.rear = new
        self.size += 1
    
    def deleteFront(self):
        if self.front is None:
            return "Queue is empty"
        
        val = self.front.data
        temp = self.front.next
        if temp:
            self.front.next = None
            temp.prev = None
        self.front = temp
        self.size -= 1
        return val
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def insertFront(self, val):
        new = Node(val)
        if self.front is None:
            self.rear = new
        else:
            self.front.prev = new
            new.next = self.front
        self.front = new
        self.size += 1
        
    def deleteRear(self):
        if self.rear is None:
            return "Deque is empty"
        val = self.rear.data
        temp = self.rear.prev
        if temp:
            temp.next = None
            self.rear.prev = None
        self.rear = temp
        self.size -= 1
        return val
    
    def getFront(self):
        if self.size == 0:
            return None
        return self.front.data
    
    def getRear(self):
        if self.size == 0:
            return None
        return self.rear.data
    
    def display(self):
        temp = self.front
        while temp:
            print(temp.data,end = ' ')
            temp = temp.next
        print()
    
d = Deque()
d.insertRear(10)
d.insertRear(20)
d.insertFront(30)
d.insertFront(40)
d.insertFront(50)
d.display()
print(d.deleteFront())
print(d.deleteRear())
d.display()
print(d.get_size())
print(d.getFront())
print(d.getRear())