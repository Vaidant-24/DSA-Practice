def help(n):
  x = 0
  while ((1<<x) <= n):          # 1<<x means 2 raise power x
    x += 1
  return x - 1 

def countSetBits(n):
  if n == 0:
    return 0
  
  if n == 1:
    return 1
  
  x = help(n)
  total = 0
  sumTill2raisePowerX = (1 << (x-1)) * x          # means 2 raise power x-1 multiply by x
  remaningSum = n - (1<<x) + 1                    
  rem = n - (1<<x)
  
  total += sumTill2raisePowerX + remaningSum + countSetBits(rem)
  
  return total
  
  
print(countSetBits(4))