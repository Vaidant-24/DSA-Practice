def genSubset(ip, op, res):
  if len(ip) == 0:
    if op not in res:
      res.append(op)
    return 
    
  op1 = op
  op2 = op + ip[0]
  ip1 = ip[1:]
  
  genSubset(ip1,op1,res)
  genSubset(ip1,op2,res)
  
  return res  

print(genSubset("abc","",[]))