arr = [1,2,3,4,5]
def pA(arr,n):
    if n == 0:
        return 
    pA(arr,n-1)
    print(arr[n-1])
    
pA(arr,5)