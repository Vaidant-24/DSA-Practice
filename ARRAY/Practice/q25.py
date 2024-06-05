# sort an array of 0's , 1's and 2's:-

nums = [2,0,2,1,1,0]
# output = [0,0,1,1,2,2]

# Using Brute force:-
def Sortarray(nums):
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(Sortarray(nums))

# Two Pointer:-

def sortArrayPointer(nums):
    n = len(nums)
    left = 0
    min = float('inf')
    right = left + 1
    while left < right and right < n:
        if nums[left] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right = left + 1
        else:
            while right < n:
                if min > nums[right]:
                    min = nums[right]
                    index = right
                right += 1
            if nums[left] < min:
                nums[left],nums[index] = nums[index],nums[left]
            left += 1
            right = left + 1
            min = -1

    return nums

print(sortArrayPointer(nums))

# Better :-
def sortArrayBetter(nums):
    n = len(nums)
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in range(n):
        if nums[i] == 0:
            count_0 += 1
        elif nums[i] == 1:
            count_1 += 1
        elif nums[i] == 2:
            count_2 += 1

    for i in range(0, count_0):
        nums[i] = 0
    
    for i in range(count_0, count_0 + count_1):
        nums[i] = 1
    
    for i in range(count_0 + count_1, n):
        nums[i] = 2
    
    return nums

print(sortArrayBetter(nums))

# Using DNF Algorithm:-
def sortArrayOptimal(nums):
    n = len(nums)
    low = 0
    mid = 0
    high = n-1

    while low < mid and mid < high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        
        elif nums[mid] == 1:
            mid += 1
        
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums 

print(sortArrayOptimal(nums))