def deleteMiddle(st):
  if len(st) == 0:
    return []
  
  k = (len(st)//2) + 1 
  solve(st,k)
  return st

def solve(st,k):
  if k == 1:
    st.pop()
    return 
  
  store = st.pop()
  solve(st,k-1)
  st.append(store)
  
  return 
5


st = [1,2,3,4,5,6]
print(deleteMiddle(st))