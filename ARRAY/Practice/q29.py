# ReArrange array elements by sign:-
nums = [1,2,-3,-1,4,5,-2,3]
def ReArrange(nums):
    n = len(nums)
    pos = []
    neg = []
    for i in range(n):
        if nums[i] > 0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])

    if len(pos) > len(neg):
        for i in range(len(neg)):
            nums[2*i] = pos[i]
            nums[2*i + 1] = neg[i]
        index = len(neg) * 2
        for i in range(len(neg),len(pos)):
            nums[index] = pos[i]
            index += 1
    else:
        for i in range(len(pos)):
            nums[2*i] = pos[i]
            nums[2*i + 1] = neg[i]
        index = len(pos) * 2
        for i in range(len(pos),len(neg)):
            nums[index] = neg[i]
            index += 1
    return nums

print(ReArrange(nums))

# def ReArrangeBetter(nums):
#     n = len(nums)
#     pos = 0
#     neg = 1
#     ans = [0]* n
#     for i in range(n):
#         if nums[i] > 0:
#             ans[pos] = nums[i]
#             pos += 2
#         else:
#             ans[neg] = nums[i]
#             neg += 2

#     return ans

# print(ReArrangeBetter(nums))

