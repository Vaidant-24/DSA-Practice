#  Left Roatate an Array:-

nums = [1,2,3,4,5,6,7]

# Using better approach:-
def rightShift(nums,k):
    n = len(nums)
    k = k % n
    temp = []
    for i in range(0,k):
        temp.insert(i,nums[n-k+i])
    for i in range(n-1,k-1,-1):
        nums[i] = nums[i - k]
    for i in range(0,k):
        nums[i] = temp[i]

    return nums
    
# Using Optimal :-
def reverseList(ls, start, end):
    ls[start:end+1] = reversed(ls[start:end+1])

nums = [-1,-100,3,99]
def rightShiftOptimal(nums, k):
        n = len(nums)
        k = k%n
        nums[0:n] = reversed(nums[0:n])
        nums[0:k] = reversed(nums[0:k])
        nums[k:n] = reversed(nums[k:n])
        return nums
print(rightShiftOptimal(nums,5))