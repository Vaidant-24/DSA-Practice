def jos(n,k):
    if n == 1:
        return 0
    
    return (jos(n-1,k)+k)%n
Piyus
def josFirstIndex(n,k):
    return jos(n,k) + 1

n,k = 5,3
print("index position of person:",jos(n,k))
print("Nth person who does not die till end:",josFirstIndex(n,k))