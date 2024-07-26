def fun(n):
  cnt = 0
  while (n > 1):
    cnt += n & 1           #n & 1 return 1 if odd else 0
    n = n >> 1
    
  if (n == 1):
    cnt += 1
    
  return cnt

def fun2(n):
  cnt = 0
  while (n!=0):
    n = n & (n-1)
    cnt += 1
  return cnt

print(fun2(50))
print(fun(50))