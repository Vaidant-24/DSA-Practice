St = [2,4,1,5,3]
def revStack(St):
  if len(St) == 1:
    return
  
  store = St.pop(0)
  revStack(St)
  St.append(store)
  return St
  
print(revStack(St))