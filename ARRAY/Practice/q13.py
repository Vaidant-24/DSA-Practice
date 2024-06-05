# 3Sum :-
nums = [-2,0,1,1,2]
# Using Brute force:-
def threeSum(nums):       # T.C = O(n^3)
                          # S.C = O(n^3)
    ans = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if i != j and i != k and j != k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        temp.sort()
                        ans.append(temp)
                        unique_set = {tuple(inner_list) for inner_list in ans} #filter out duplicates in list with the help of SET
    return unique_set

# Using Better Optimization:-
def threeSumBetter(nums):            # T.C = O(n^2)
                                    # S.C = O(n^2)
    ans = []
    n = len(nums)
    for i in range(n):
        hashMap = []
        for j in range(i+1,n):
            third = -(nums[i] + nums[j])
            if third in hashMap: 
                lst = [nums[i], nums[j], third]
                lst.sort()
                ans.append(lst)
                unique_set = {tuple(inner_list) for inner_list in ans}   
            else:
                hashMap.append(nums[j])
    return unique_set

# print(threeSumBetter(nums))

# Using Best Optimization:-

def threeSumBest(nums):     # O(n^2)
    ans = []                # O(1)
    n = len(nums)
    nums.sort()  
    for i in range(n):
        if ( i > 0 and nums[i] == nums[i-1]):
            continue
        j = i + 1
        k = n - 1
        while(j < k):
            sum = nums[i] + nums[j] + nums[k]

            if sum < 0:
                j += 1
            elif sum > 0:
                k -= 1
            else:
                temp = [nums[i], nums[j], nums[k]]
                ans.append(temp)
                
                while(j < k and nums[j] == nums[j+1]): 
                    j += 1
                while(j < k and nums[k] == nums[k-1]):
                    k -= 1
                j += 1
                k -= 1
    return ans

print(threeSumBest(nums))