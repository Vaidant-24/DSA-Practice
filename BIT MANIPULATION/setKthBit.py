def setKthBit(n,k):
  b = bin(n)
  l = len(b[2:])
  if k < l:
    st = str(b[2:])
    return st[l - (k + 1)] == '1'
  return "Out Of Range"
print(setKthBit(31,5))
  