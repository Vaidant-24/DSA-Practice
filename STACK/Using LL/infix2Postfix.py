class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def push(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        else:
            pop_val = self.head.data
            self.head = self.head.next
            return pop_val

    def peek(self):
        if self.head is None:
            return "Stack is empty"
        return self.head.data

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

