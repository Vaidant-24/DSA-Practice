n = 10010

def fun(n):
  if n == 0 or n & 1 == 0:
    return "Even"
  else:
    return "Odd"
  
print(fun(n))
    