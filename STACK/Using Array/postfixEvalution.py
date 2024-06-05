def evaluatePostfix(postfix):
    stack = []
    for i in postfix.split():
        if i.isdigit():
            stack.append(i)
        elif i in ['+', '-', '*', '/', '^']:
            if len(stack) < 2:
                return "Invalid Expression"
            op1 = int(stack.pop())
            op2 = int(stack.pop())
            if i == '+':
                result = op2 + op1
            elif i == '-':
                result = op2 - op1
            elif i == '*':
                result = op2 * op1
            elif i == '/':
                result = op2 / op1
            elif i == '^':
                result = op2 ** op1
            stack.append(result)
        else:
            return "Invalid Expression"
    return stack.pop()
    
postfix = "10 2 6 * 8 + -"
print(evaluatePostfix(postfix))
            