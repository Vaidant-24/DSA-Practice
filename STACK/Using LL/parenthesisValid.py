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


def isMatch(b, a):
    if (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}'):
        return True
    else:
        return False


def checkParenthesis(st, stri):
    for i in stri:
        if i == '{' or i == '[' or i == '(':
            st.push(i)
        elif i == '}' or i == ']' or i == ')':
            if st.isEmpty():
                return False
            elif not isMatch(i, st.peek()):
                return False
            else:
                st.pop()
    if st.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    st = Stack()
    stri = "{}{}{}"
    print(checkParenthesis(st, stri))
