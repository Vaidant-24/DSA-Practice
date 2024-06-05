from array import *

a1 = array('i',[23,4,45,6,56])
def search(array, element):
    flag = 0
    for i in range(len(array)):
        if array[i] == element:
            flag = 1
            return i
    if flag == 0:
        return -1

def delete(array, element):
    i = search(array, element)
    if i != -1:
        for x in range(i, len(array)-1):
            array[x] = array[x+1]
        array[-1] = 0
    else:
        print("No such element found!")
# with the help of pop():-
# def delete(array, element):
#     i = search(array, element)
#     if i != -1:
#         array.pop(i)
#     else:
#         print("No such element found!")

# delete(a1,4)
# print(a1)
# delete(a1,23)
# print(a1)
delete(a1,45)
print(a1)
delete(a1,23)
print(a1)
delete(a1,56)
print(a1)
            
            