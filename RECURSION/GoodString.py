def fun(n):
  if n == 1:
    return 5

  if (n) % 2 == 0:
    product = 4 * fun(n-1)
  elif (n) % 2 == 1:
    product = 5 * fun(n-1)
  
  return product

print(fun(4))