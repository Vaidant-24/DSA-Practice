# Remove Value:-
nums = [3,2,2,3]
def removeVal(nums, val):
    i = 0
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j

print(removeVal(nums,2))