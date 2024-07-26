def genParenthesis(n):
  o = n
  c = n
  return solve(o,c,"",[])

def solve(o,c,op,res):
    if o == 0 and c == 0:
      res.append(op)
      return
    
    if o != 0:
      solve(o-1,c,op+"(",res)
      
    if c > o:
      solve(o,c-1,op+")",res)
      
    return res

print(genParenthesis(3))