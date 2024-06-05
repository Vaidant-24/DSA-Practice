# 4Sum Problem :

nums = [1,0,-1,0,-2,2]
# Using self approach :-
def fourSum(nums,target):
    n = len(nums)
    nums.sort()
    ans = []
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i+1]:
                continue
        j = i + 1
        k = j + 1
        l = n - 1

        while (j < k and k < l):
            
            sum = nums[i] + nums[j] + nums[k] + nums[l] 
            
            if sum < target:
                if k < l:
                    while(k < l and nums[k] == nums[k+1]):
                        k += 1
                    k += 1
                else:
                    while(j < k and nums[j] == nums[j+1]):
                        j += 1
                    j += 1
            elif sum > target:
                while(l > k and nums[l] == nums[l - 1]):
                    l -= 1
                l -= 1
            else:
                temp = [nums[i], nums[j], nums[k], nums[l]]
                ans.append(temp)
                
                while(j < k and nums[j] == nums[j+1]):
                    j += 1
                while(k < l and nums[k] == nums[k+1]):
                    k += 1
                j += 1
                k = j + 1
    return ans

# print(fourSum(nums, 8))

# Better Approach:-

def fourSumB(nums,target):
    n = len(nums)
    ans = []
    for i in range(n-2):
        for j in range(i+1,n-1):
            hashMap = []
            for k in range(j+1,n):
                sum = nums[i] + nums[j] + nums[k]
                fourth = target - sum
                if fourth in hashMap:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    ans.append(temp)
                    unique_set = {tuple(inner_list) for inner_list in ans}
                else:
                    hashMap.append(nums[k])
    return unique_set

# print(fourSumB(nums,0))

# Using Optimal Approach:-

def fourSumOptimal(nums, target):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(n-3):

        if i > 0 and nums[i] == nums[i-1]:
            continue

        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:
                sum = nums[i] + nums[j] + nums[k] + nums[l]
                if sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1
                elif sum < target:
                    k += 1
                    while k < l and nums[k] == nums[k-1]:
                        k += 1
                else:
                    l -= 1
                    while k < l and nums[l] == nums[l+1]:
                        l -= 1
    return ans

print(fourSumOptimal(nums,0))