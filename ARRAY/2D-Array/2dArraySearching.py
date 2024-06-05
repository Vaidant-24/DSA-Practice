import numpy as np

a1 = np.array([[1,2,3,10],[4,5,6,20],[7,8,9,30]])

def search(array,element):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i,j] == element:
                return i,j
    return "Element not found!"

print(search(a1,30))