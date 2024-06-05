st = "aabbaa"

def checkPallindrome(st):
    res = st[::-1]
    return res == st

def checkPallindromeIterative(st):
    l = 0
    h = len(st)-1
    
    while l < h:
        if st[l] != st[h]:
            return False
        else:
            l += 1  
            h -= 1
    return True

print(checkPallindrome(st))
print(checkPallindromeIterative(st))