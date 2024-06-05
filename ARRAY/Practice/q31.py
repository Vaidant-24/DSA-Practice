# Find Team Leader:-
nums = [10, 22, 12, 3, 0, 6]

def leader(nums):
    ans = []
    n = len(nums)
    for i in range(n):
        flag = 0
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                flag = 1
                break
        
        if flag == 0:
            ans.append(nums[i])
    return ans

print(leader(nums))

def leaderOptimal(nums):
    ans = []
    n = len(nums)
    elem = nums[n-1]
    ans.append(elem)
    for i in range(n-2,-1,-1):
        if nums[i] > elem:
            ans.append(nums[i])
            elem = nums[i]
    ans[0:n] = reversed(ans[0:n])
    return ans
print(leaderOptimal(nums))            