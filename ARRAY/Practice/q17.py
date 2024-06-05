# Largest ELement in an Array:-

nums = [4,6,7,3,9,5,1,2]

# Brute force Approach:-
def getLarge(nums):
    n = len(nums)
    if n == 0 or n == 1:
        return -1
    nums.sort()
    return nums[len(nums)-1]

# Optimal Approach:-
def getLargest(nums):
    n = len(nums)
    if n == 0 or n == 1:
        return -1
    max = -float('inf')

    for i in nums:
        if i > max:
            max = i
    return max

# print(getLargest(nums)) 

# 2nd Largest Element:-

# Brute force Approach:-

def getSecondLarge(nums):
    n = len(nums)
    if n == 0 or n == 1:
        return -1
    nums.sort()
    lar = nums[len(nums)-1]
    small = nums[0]
    n = len(nums)
    for i in range(n-2,-1,-1):
        if nums[i] != lar:
            secondLar = nums[i]
            break
        else:
            return -1
    for i in range(1, n):
        if nums[i] != small:
            secondSmall = nums[i]
            break
        else:
            return -1
    return secondLar,secondSmall

# Better Approach:-

def getSecondLargest(nums):
    n = len(nums)
    lar = -float('inf')
    small = float('inf')
    for i in range(n):
        if nums[i] > lar:
            lar = nums[i]
    
    secLar = -float('inf')
    for i in range(n):
        if nums[i] > secLar and nums[i] != lar:
            secLar = nums[i]

    for i in range(n):
        if nums[i] < small:
            small = nums[i]
    
    secSmall = float('inf')
    for i in range(n):
        if nums[i] < secSmall and nums[i] != small:
            secSmall = nums[i]

    return secLar, secSmall 

def getSecondLargestO(nums):
    n = len(nums)
    lar = nums[0]
    secLar = -float('inf')
    small = nums[0]
    secSmall = float('inf')
    
    for i in range(1,n):
        if nums[i] > lar:
            secLar = lar
            lar = nums[i]
        elif nums[i] < lar and secLar < nums[i]:
            secLar = nums[i]
    for i in range(1,n):
        if nums[i] < small:
            secSmall = small
            small = nums[i]    
        elif nums[i] > small and secSmall > nums[i]:
            secSmall = nums[i]
    return secLar, secSmall

print(getSecondLargestO(nums))


