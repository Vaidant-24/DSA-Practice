# Count Subarray sum Equals K:-
nums = [3,1,2,4]

def countSubArray(nums,sum):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i,n):
            preSum = 0
            for k in range(i,j+1):
                preSum += nums[k]
            if preSum == sum:
                count += 1
                
    return count

print(countSubArray(nums,6))

def countSubArrayBetter(nums,sum):
    n = len(nums)
    count = 0
    for i in range(n):
        preSum = 0
        for j in range(i,n):
            preSum += nums[j]
            if preSum == sum:
                count += 1
    return count

print(countSubArrayBetter(nums,6))


def countSubArrayOptimal(arr,k):
    n = len(arr) # size of the given array.
    mpp = {0:1}
    preSum = 0
    cnt = 0

    for num in arr:
        # add current element to prefix Sum:
        preSum += num

        # Calculate x-k:
        remove = preSum - k

        # Add the number of subarrays to be removed:
        if remove in mpp:
            cnt += mpp[remove]  # return the dict value if exist,
                                # otherwise return 0
        if preSum in mpp:       # Update the count of prefix sum
            mpp[preSum] += 1    # in the map.
        else:
            mpp[preSum] = 1
                                    
        
    return cnt

print(countSubArrayOptimal(nums, 6))