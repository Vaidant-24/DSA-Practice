# Check Array is Sorted:-
nums = [2,3,4,5,6,8,6,7]
def isSorted(nums):
    n = len(nums)
    for i in range(1,n):
        if nums[i] < nums[i-1]: 
            return False
    return True

print(isSorted(nums))

