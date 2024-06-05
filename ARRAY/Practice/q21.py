# Find the number that appears once, and the other numbers twice:-
nums = [4,1,2,2,1,3,3]
def numOnce(nums):
    n = len(nums)
    m = max(nums)
    hashMap = [0] * (m+1)

    for i in range(n):
        hashMap[nums[i]] += 1

    for i in range(len(hashMap)):
        if hashMap[i] == 1:
            return i

print(numOnce(nums))

#Using Stack:-

def numOnceB(nums):
    n = len(nums)
    hashMap = []
    nums.sort()
    for i in range(n):
        if nums[i] not in hashMap:
            hashMap.insert(i, nums[i])
        else:
            hashMap.pop()
    return hashMap[0]

print(numOnceB(nums))

#Using XOR operation:-
# Note:-
# a^a = 0
# a^0 = a

def numOnceOp(nums):
    xor = 0

    for i in nums:
        xor ^= i
    
    return xor

print(numOnceOp(nums))
