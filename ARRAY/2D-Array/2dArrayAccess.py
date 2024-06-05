import numpy as np

a1 = np.array([[1,2,3],[4,5,6],[7,8,9]])

def get_element(array, i , j):
    if i < len(array) and j < len(array):
        print(array[i][j])
    else:
        print("Index out of range!")
get_element(a1,0,2)
get_element(a1,1,2)
get_element(a1,3,3)