def fun(arr):
  n = len(arr)
  ans = 0
  for i in range(0,n):
    ans += arr[i] * (2 ** (n - (i+1)))
    
  return ans

print(fun([1,1]))