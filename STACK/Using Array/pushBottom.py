def pushBottom(stack,value):
    if not stack:
        stack.append(value)
        
        return 
    temp = stack.pop()
    pushBottom(stack,value)
    stack.append(temp)
    
stack = [1,2,3]
pushBottom(stack,4)
print(stack)