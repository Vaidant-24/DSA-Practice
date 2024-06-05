# Find the majority element that occurs more than N/2 times in an array:-

# Brute force:-
nums = [2,2,1,1,1,2,2]
def majorElement(nums):
    n = len(nums)
    count = 0
    print("len is:",n)
    print("N/2 is:",n//2)
    for i in range(n-1):
        count =1
        for j in range(i+1,n):
            if nums[j] == nums[i]:
                count += 1
        if count > n//2:
            return nums[i]
        

print(majorElement(nums))

# Using HashMap:-
def majorElementBetter(nums):
    n = len(nums)
    m = max(nums)
    hashMap = [0] * (m+1)
    for i in range(n):
        hashMap[nums[i]] += 1
    for i in range(m+1):
        if hashMap[i] > (n//2):
            return i

print(majorElementBetter(nums))
# Using Counter:-
# from collections import Counter

# nums = [1,3,1,2,1,3,3,1,1,1]
# def majorElementBetter(nums):
#     count = Counter(nums)
#     print(count)
    
#     for num, count in count.items():
#         if count > (len(nums)//2):
#             return num
        
# print(majorElementBetter(nums))

# Optimal Solution:-
# Using Moore's Voting algorithm:-
def majorElementOptimal(nums):
    n = len(nums)
    cnt = 0
    for i in range(n):  
        if cnt == 0:
            cnt = 1
            elem = nums[i]

        elif nums[i] == elem:
            cnt += 1

        else:
            cnt -= 1

    if nums.count(elem) > n//2:
        return elem 
    else:
        return -1  
        
print(majorElementOptimal(nums))

# def majorElementOptimal(nums):
#         n = len(nums)
#         nums.sort()
#         ct = nums.count(nums[n//2])
#         if ct > n//2:
#             return nums[n//2]
