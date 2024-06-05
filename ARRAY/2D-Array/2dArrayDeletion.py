import numpy as np

a1 = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(a1)

a2 = np.delete(a1, 0 , axis = 0)    # O(mn)
print(a2)

a3 = np.delete(a1, 0 , axis = 1)    # O(mn)
print(a3)

a4 = np.delete(a1, 2 , axis = 1)    # O(1)
print(a4)