def jos(n,k):
    if n == 1:
        return 0
    
    return (jos(n-1,k)+k)%n

def josFirstIndex(n,k):
    return jos(n,k) + 1

print(jos(5,3))
print(josFirstIndex(5,3))