def rec(n):
    if n < 10:
        return n
    
    return rec(n//10) + n%10
    
print(rec(283))