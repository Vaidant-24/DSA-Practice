# Two Sum - II 
# Given array is sorted 
nums = [1,3,4,5,7,10,11]

def twoSum(nums,target):
    l = 0
    r = len(nums) - 1
    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            return [l+1 , r+1]

print(twoSum(nums,9))