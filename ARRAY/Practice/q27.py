# find Maximum Subarray sum in an array:- (Contigous SubArray)

nums = [-1,-3,-2]
# brute force:-
def MaxSubArray(nums):
    n = len(nums)
    presum = 0
    maxi = -float('inf')

    for i in range(n):
        for j in range(i,n):
            presum = 0
            for k in range(i,j):
                presum += nums[k]
                maxi = max(maxi,presum)

    return maxi

print(MaxSubArray(nums))

# Better:-
def MaxSubArrayBetter(nums):
    n = len(nums)
    maxi = -float('inf')
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]
            maxi = max(maxi,sum)

    return maxi

print(MaxSubArrayBetter(nums))

# Optimal:-
def MaxSubArrayOptimal(nums):
    n = len(nums)
    maxi = -float('inf')
    sum = 0
    for i in range(n):
        sum += nums[i]
        maxi = max(sum, maxi)
        if sum < 0:
            sum = 0
        
    return maxi

print(MaxSubArrayOptimal(nums))
            