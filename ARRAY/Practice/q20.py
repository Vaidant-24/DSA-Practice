# Move all zeroes to the end of the array:-
nums = [1,0,2,3,0,4,0,1]
def moveZeroesToRight(nums):
    n = len(nums)
    for i in range(n-1):
        if nums[i] == 0:
            for j in range(i+1, n):
                if nums[j] != 0:
                    nums[i],nums[j] = nums[j],nums[i]
                    break
                elif nums[j] == 0 and j == n-1:
                    break
    return nums

print(moveZeroesToRight(nums))

# Find if element is present in array and return index:-
arr = [1,2,3,4,5]
def indexSearch(nums, elem):
    n  = len(nums)
    for i in range(n):
        if elem == nums[i]:
            return i
    return -1
    
print(indexSearch(arr, 3))
print(indexSearch(arr,6))


