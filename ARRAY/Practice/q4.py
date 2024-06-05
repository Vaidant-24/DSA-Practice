# Find maximum product of two positive integers in array

import numpy as np
myArray = np.array([1,20,30,44,5,56,57,8,9,10,31,12,13,14,35,16,27,58,19,21])

def max_product(myArray):
    max = 0
    for i in range(len(myArray)):
        for j in range(i+1,len(myArray)):
            if myArray[i] * myArray[j] > max:
                max = myArray[i] * myArray[j]
                pair = str(myArray[i]) + "," + str(myArray[j])
    print(pair)
    print(max)

max_product(myArray)