nums = [1,2,3]
def fun(nums):
  n = len(nums)
  ans = []
  for i in range(1<<n):
    subset = []
    for j in range(n):
      if i & (1<<j):       #Check if jth bit is set or not, of number(i)
        subset.append(nums[j])
    ans.append(subset)
  return ans

print(fun(nums))