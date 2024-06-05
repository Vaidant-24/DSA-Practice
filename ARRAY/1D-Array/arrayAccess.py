from array import *

a1 = array('i',[4,25,61,63])

def get_element(array, index):
    if index >= len(array):
        print('index out of range!')
    else:
        print(array[index])
    
get_element(a1,3)