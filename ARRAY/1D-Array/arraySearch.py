from array import *

a1 = array('i',[23,4,45,6,56])
def search(array, element):
    flag = 0
    for i in range(len(array)):
        if array[i] == element:
            flag = 1
            print("element found at index:{}".format(i))
            break
    if flag == 0:
        print("No element found!")

search(a1,45)
search(a1,4)
search(a1,23)
search(a1,56)
search(a1,100)
