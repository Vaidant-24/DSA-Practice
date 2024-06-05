# Matrix Transposition

import numpy as np

myArray = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(myArray)
# def tranpose(myArray):
#     matrix = np.array(myArray)
#     n = len(myArray)
#     for i in range(n):
#         for j in range(n):
#             matrix[i,j] = myArray[j,i]
#     return matrix
# print(tranpose(myArray))

def trans(myArray):
    matrix = np.array(myArray)
    n = len(myArray)
    for i in range(n-2):
        for j in range(i+1,n-1):
            matrix[i,j] = myArray[j,i]
    return matrix

print(trans(myArray))