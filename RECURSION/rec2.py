def rec(i):
    if i == 0:
        return 
    rec(i-1)
    print(i)
    rec(i-1)
    
rec(3)