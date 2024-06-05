# Find closest threeSum:

nums = [-1,2,1,-4]

# Using Brute force:-
def closest3Sum(nums,target):
    n = len(nums)
    ls = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                sum = nums[i] + nums[j] + nums[k]
                ls.append(sum)
    diff = []
    for num in (ls):
        gap = abs(num - target)
        diff.append(gap)

    dict = {}
    for i in range(n):
        dict[ls[i]] = diff[i]
    
    min_key = min(dict, key=dict.get)
    return min_key

# Using Optimal Approach:-    
def closest3SumOp(nums, target):  # TC : O(n^2)
    n = len(nums)                 # SC : O(1)
    nums.sort()
    closest_sum = float('inf')
    min_diff = float('inf')
    for i in range(n-2):
        j = i + 1
        k = n -1
        while(j < k):
            cur_sum = nums[i] + nums[j] + nums[k]
            diff = abs(cur_sum - target)

            if diff < min_diff:
                min_diff = diff
                closest_sum = cur_sum
            
            if cur_sum < target:
                j += 1

            elif cur_sum > target:
                k -= 1

            else:
                return cur_sum
    return closest_sum

print(closest3SumOp(nums, 1))
