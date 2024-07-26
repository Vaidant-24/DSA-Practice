def set(n,k):
  print(bin(n))
  print(bin(n | (1<<k)))

def clear(n,k):
  print(bin(n))
  print(bin(n & ~(1<<k)))
  
  
set(9,2)
clear(9,2)

def toggle(m):
  print(bin(m))
  print(bin(m ^ (1<<2)))
  


