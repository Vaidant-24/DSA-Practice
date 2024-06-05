# Rotate Matrix by 90 clockwise:-

import numpy as np

myArray = np.array([[2,5,3],[1,8,7],[6,9,4]])
print(myArray)

# Using Brute Force Method:-
# def rotateMatrix(myArray):              TC : 0(n^2)
#     matrix = np.array(myArray)          SC : 0(n^2)
#     n = len(myArray)
#     for i in range(n):
#         for j in range(n):
#             matrix[j, (n-1)-i] = myArray[i,j]
#     return matrix

# Using Transposition Approach:-

# def rotateMatrix(myArray):
#     n = len(myArray)
#     matrix1 = np.transpose(myArray)
#     matrix2 = np.array(myArray)
#     for i in range(n):
#         for j in range(n):
#             matrix2[i,j] = matrix1[i,(n-1) - j]
#     return matrix2
# print(rotateMatrix(myArray))

# Using Optimal Approach means without using another matrix with the help of
# def rotate_matrix(matrix):
#     n = len(matrix)
    
#     # Transpose the matrix
#     for i in range(n):
#         for j in range(i, n):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
#     # Reverse each row
#     for i in range(n):
#         matrix[i].reverse()
    
#     return matrix



# rotated_matrix = rotate_matrix(myArray)
# for row in rotated_matrix:
#     print(row)
    
# Optimal Approach using array:-
def rotateMatrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n - layer - 1
        for i in range(first, last): # i = 0(corner element) and i = 1(middle element)
            # save top element
            top = matrix[layer][i]
            # move left element to top
            matrix[layer][i] = matrix[-i-1][layer]
            # move bottom element to left
            matrix[-i-1][layer] = matrix[-layer-1][-i-1]
            # move right element to bottom
            matrix[-layer-1][-i-1] = matrix[i][-layer-1]
            # move top element to right
            matrix[i][-layer-1] = top
        return matrix
    
print(rotateMatrix(myArray))