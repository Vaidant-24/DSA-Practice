# Next Permutation:-
nums = [2,1,3]

def nextPermutation(nums):
    n = len(nums)
    ind = -1
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            ind = i
            break

    if ind == -1:
        nums.reverse()
        return nums    
    else:
        for i in range(n-1,ind,-1):
            if nums[i] > nums[ind]:
                nums[ind],nums[i] = nums[i],nums[ind]
                break
        
    nums[ind+1:n] = reversed(nums[ind+1:n])

    return nums

print(nextPermutation(nums))