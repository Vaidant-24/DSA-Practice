# Find the longest sub array in the given array:-

nums = [1,2,3,1,1,1,1]
#output = 2(length of longest sub array which is : [2,3])

# Using Better Approach:-
def maxSubArray(nums, k):
    hashMap = {}
    n = len(nums)
    maxLen = 0
    sum = 0

    for i in range(n):
        sum += nums[i]

        if sum == k:
            maxLen = max(maxLen, i+1)
        
        rem = sum - k
        if rem in hashMap:
            lens = i - hashMap[rem]
            maxLen = max(lens,maxLen)

        if sum not in hashMap:
            hashMap[sum] = i

    return maxLen

print(maxSubArray(nums,5))

# Using Optimal Approach:-

def maxSubArrayOp(nums, k):
    left = right = 0
    sum = nums[0]
    maxLen = 0
    n = len(nums)

    while right < n:
        right += 1
        if right < n:
            sum += nums[right]
        
        if sum == k:
            maxLen = max(maxLen,(right - left + 1))

        while left <= right and sum > k:
            sum -= nums[left]
            left += 1

    return maxLen

print(maxSubArrayOp(nums, 5))
     
