s = "Brain"

# Output : RANI

def SwapLast2(s):
    if len(s) == 0:
        print(" ")
    elif len(s) == 1:
        print(s[0])
    else:
        temp = s[-1] + s[-2] 
        l = len(s)-2
        temp2 = s[0:l]
        print(temp2 + temp)      
        
SwapLast2(s)