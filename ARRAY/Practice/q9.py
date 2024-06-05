# Remove duplicate from sorted array

nums = [0,0,1,1,1,2,2,3,3,4]

#Leetcode Accepted:-
def removeDuplicates(nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
        


# def removeDuplicates(nums):
#     n = len(nums)
#     count = 0
#     hashMap = []
#     for i,num in enumerate(nums):
#         if num in hashMap:
#             count += 1
#         else:
#             hashMap.append(num)
#     return count,hashMap

print(removeDuplicates(nums))