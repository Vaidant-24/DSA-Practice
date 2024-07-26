def numToBin(n):
  res = ""
  while (n != 1):
    if n % 2 == 1:
      res = '1' + res
    else:
      res =  '0' + res
    n = n // 2
  return '1' + res

def BinToNum(bin):
  n = len(bin)
  res = 0
  for i in range(n-1,-1,-1):
    res += int(bin[i]) * (2 ** (n-i-1))
  return res

def BinToNumEff(bin):
  n = len(bin)
  sum = 0
  p2 = 1
  for i in range(n-1,-1,-1):
    if bin[i] == '1':
      sum +=  p2
    p2 *= 2
  return sum  
print(numToBin(13))
print(BinToNum('1101')) 
print(BinToNumEff('1101'))