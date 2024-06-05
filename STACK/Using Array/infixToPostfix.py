def precedence(char):
    if char == '+' or char == '-':
        return 1
    if char == '*' or char == '/':
        return 2
    if char == '^':
        return 3
    return 0

def infixToPostfix(infix):
    postfix = []
    stack = []
    for i in infix:
        if i.isalnum():   # if 'i' is operand
            postfix.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # remove '('
        else:    # operator
            while stack and precedence(i) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(i)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)

infix = "a+b/c-d*e"
print(infixToPostfix(infix))
