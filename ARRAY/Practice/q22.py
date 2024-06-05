# Find most consecutive occurrences of 1's:-
nums = [1,1,1,1,1,0,1,1]
# Self-Approach:-
def mostConsecutiveOnes(nums):
    n = len(nums)
    j = -1
    lst = []
    for i in range(n):
        if nums[i] == 1:
            j = i
            break
    flag = 0
    for i in range(n):
        if nums[i] == 0:
            flag = 1

    if flag != 1:            # If list has only 1's (Not a single 0)
        return nums.count(1)
    
    if j == -1:              # If list has only 0's (Not a single 1)
        return 0
    count = 1
    for i in range(j+1,n):

        if nums[i] == 1:
            count += 1
            j += 1
        elif nums[i] == 0:
            lst.append(count)
            count = 0
            j += 1
    lst.append(count)
        
    ans = max(lst)
    return ans

print(mostConsecutiveOnes(nums))

# Using Count and Max_count:-

def ConsecutiveOnes(nums):
    n = len(nums)
    j = -1
    k = -1
    for  i in range(n):
        if nums[i] == 1:
            j = i
            break
    if j == -1:
        return 0
    
    for i in range(n):
        if nums[i] == 0:
            k = 1
    if k == -1:
        return nums.count(1)

    count = 1
    max_count = 1

    for i in range(j+1,n):
        if nums[i] == 1:
            count += 1
        elif nums[i] == 0:
            count = 0
        max_count = max(count,max_count)
    return max_count

print(ConsecutiveOnes(nums))

#Using Striver Approach :-
def NumConsecutiveOnes(nums):
        cnt = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi, cnt)
        return maxi

print(NumConsecutiveOnes(nums))