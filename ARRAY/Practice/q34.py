# Return the Spiral Matrix:-
nums  = [[1,2,3,4],
         [5,6,7,8],
         [9,10,11,12],
         [13,14,15,16]]

def SpiralMatrix(nums):
    row = len(nums)
    col = len(nums[0])

    top = 0
    left = 0
    right = col - 1
    bottom = row - 1

    ans = []

    while(left <= right and top <= bottom):
        for i in range(left, right+1):
            ans.append(nums[top][i])
        top += 1

        for i in range(top, bottom+1):
            ans.append(nums[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left-1,-1):
                ans.append(nums[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom,top-1,-1):
                ans.append(nums[i][left])
            left += 1

    return ans

print(SpiralMatrix(nums))