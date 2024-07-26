def sorted(arr):
  if len(arr) == 1:
    return 
  
  store = arr.pop()
  sorted(arr)
  
  if len(arr) == 0:
    arr.append(store)
  else:
    for i in range(len(arr)):
      if arr[i] > store:
        arr.insert(i,store)
        return arr
    arr.append(store)
  
  return arr
   
# arr = [1,3,5,2]
# print(sorted(arr))

arr = [1,3,5,2]

def sortFun(arr):
  if len(arr) == 1:
    return arr
  
  store = arr.pop()
  arr = sortFun(arr)
  insertFun(arr, store)
  return arr

def insertFun(arr, store):
  if len(arr) == 0 or arr[len(arr) - 1] <= store:
    arr.append(store)
    return arr

  temp = arr.pop()
  arr = insertFun(arr, store)
  arr.append(temp)
  return arr

print(sortFun(arr))
