def fun(n,i):
  print(bin(n))
  print(bin(n ^ (1 << i)))
  
fun(13,2)
fun(13,1)
  