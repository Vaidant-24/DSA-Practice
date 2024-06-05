import numpy as np

a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a1)

a2 = np.insert(a1,0,[10,11,12],axis=1) # axis = 1 for column-number
a3 = np.insert(a1,0,[10,11,12],axis=0) # axis = 0 for row-number
print(a2)
print(a3)

a4 = np.insert(a1,1,[13,14,15],axis=0) 
a5 = np.insert(a1,1,[13,14,15],axis=1) 
print(a4)
print(a5)

newA = np.array([[10,20,30],[40,50,60],[70,80,90]])
a6 = np.append(newA,[[17,18,19]],axis=0)
a7 = np.append(newA,[[17,18,19]],axis=0) 
print(a6)
print(a7)