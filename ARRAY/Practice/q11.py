height = [1,8,6,2,5,4,8,3,7]

# Using Brute Force :   O(n^2)
def max_water(height):
    n = len(height)
    res = 0
    for i in range(n-1):
        for j in range(i+1,n):
            area = min(height[i], height[j]) * (j - i)
            res = max(res, area)
    return res


# Using Optimal Solution(Two Pointer) : O(n)

def max_area(height):
    l = 0
    r = len(height) - 1
    res = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        res = max(res,area)

        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
        
    return res
    
print(max_area(height))