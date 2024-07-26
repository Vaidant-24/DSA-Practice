def kthGrammar(n,k):
  if n == 1 and k == 1:
    return 0
    
  mid = 2**(n-2)
  if k <= mid:
    return kthGrammar(n-1, k)
  else:
    ans = 1 - kthGrammar(n-1, k - mid)      
  return ans
  
print(kthGrammar(3,4))