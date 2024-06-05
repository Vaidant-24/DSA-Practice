nums = [1,2,0,1]

def lonSeqBetter(nums):
    n = len(nums)
    nums.sort()
    count = 0
    lastSmaller = -float('inf')
    maxi = 0
    if n == 0:
        return 0
    else:
        for i in range(n):
            if nums[i] - 1 == lastSmaller:
                count += 1
                lastSmaller = nums[i]
            elif nums[i] != lastSmaller:
                count = 1
                lastSmaller = nums[i]
            maxi = max(maxi,count)
        return maxi

print(lonSeqBetter(nums))

def lonSeqOptimal(nums):
    n = len(nums)
    if n == 0: return 0
    cnt = 0
    maxi = 0
    st = set(nums)
    for it in nums:
        if it - 1 not in st:
            cnt = 1
            x = it
            while x+1 in st:
                x += 1
                cnt += 1
            maxi = max(maxi,cnt)
    return maxi

print(lonSeqOptimal(nums))