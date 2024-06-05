import numpy as np

a1 = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
print(a1[0][2])
print(a1[0,2])
print('\n')
print(len(a1)) # return number of rows
print(len(a1[0])) # return number of columns
print('\n')
for i in range(len(a1)):         # O(mn)
    for j in range(len(a1[0])):  # 0(n)
        print(a1[i,j],end=' ')  # O(1)
    print('\n')