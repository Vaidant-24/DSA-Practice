from array import *

def traverse(array):
    for i in array:                 # O(n)
        print(i,end=' ')

a1 = array('i',[25,65,45,43,23])
traverse(a1)