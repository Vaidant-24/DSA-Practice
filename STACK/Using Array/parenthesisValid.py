def isValid(s: str) -> bool:
    def match(a,b):
        if a == '(' and b == ')':
            return True
        elif a == '[' and b == ']':
            return True
        elif a == '{' and b == '}':
            return True
        else:
            return False
                
    stack = []
    for i in s:
        if i in ['(','[','{']:
            stack.append(i)
        else:
            if not stack:    # stack is empty
                return False
            top = stack[-1]
            if not match(top,i):
                return False
            stack.pop()
    
    if stack:
        return False
    else:
        return True
    
s = '(([{}]))'
print(isValid(s))