ls = [2,4,3,5,6,1,7,8]

def get_pair(ls,sum):   
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            if ls[i] + ls[j] == sum:
                return ls[i],ls[j]

#Using Two Pointers :-
nums = [1,2,3,4,5,6,7,8,9]
def twoSum(nums,target):
    n = len(nums)
    nums.sort()
    i = 0
    j = n - 1
    
    while(i < j):
        sum = nums[i] + nums[j]
        if sum == target:
            return nums[i], nums[j]
        elif sum < target:
            i += 1
        else:
            j -= 1
print(get_pair(ls, 10))


print(twoSum(ls,10))