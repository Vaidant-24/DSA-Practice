arr = [-3,4,-3,-1,1]

def zeroSubArray(arr):
    ans = []
    for i in range(len(arr)):
        prev = 0
        for j in range(i,len(arr)):
            if prev + arr[j] == 0:
                return True
            prev += arr[j]
    return False

def Efficient(arr):
    preSum = 0
    hashMap = {}
    for i in range(len(arr)):
        if arr[i] in hashMap or preSum == 0:
            return True
        preSum += arr[i]
        hashMap.add(arr[i])
    return False 

print(Efficient(arr))
print(zeroSubArray(arr))