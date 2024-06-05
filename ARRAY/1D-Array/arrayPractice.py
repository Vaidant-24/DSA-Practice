#1 Create an array and traverse

from array import *
print("Step 1")
a1 = array('i',[24,5,62,13,75])



for i in a1:
    print(i,end=' ')
print('\n')

#2 Access individual elements through index
print("Step 2")
print(a1[0],a1[1],a1[2])
for i in range(len(a1)):
    print(a1[i],end=' ')
print('\n')

#3 Append any value to the array using append() method
print("Step 3")
a1.append(45)
print(a1)
print('\n')

#4 Insert value in an array using insert() method
print("Step 4")
a1.insert(4,35)
print(a1)
print('\n')

#5 Extend python array using extend() method
print("Step 5")
a2 = array('i',[90,80,70,60])
a1.extend(a2)
print(a1)
print('\n')

#6 Add items from list to array using fromlist() method
print("Step 6")
list = [100,200,300]
a3 = array('i',[10,20,30,40])
a3.fromlist(list)
print(a3)
print('\n')

#7 Remove any array element using remove() method
print("Step 7")
a4 = array('i',[10,30,60,50])
a4.remove(30)
print(a4)
print('\n')

#8 Remove last array element using pop() method
print("Step 8")
a5 = array('i',[10,20,30,40])
a5.pop()
a5.pop(0)
print(a5)
print('\n')

#9 Fetch any element through its index using index() method
print("Step 9")
a6 = array('i',[90,10,20,30,40,5])
print(a6.index(20))
print('\n')

#10 Reverse a python array using reverse() method
print("Step 10")
a7 = array('i',[20,3,4,52,1])
a7.reverse()
print(a7)
print('\n')

#11 Get array buffer information through buffer_info() method
print("Step 11")
a8  = array('i',[20,3,4,52,1])
print(a8.buffer_info())
print('\n')

#12 Check for number of occurences of an element using count() method
print("Step 12")
a9 = array('i',[20,3,4,52,1,3,4,2,3])
print(a9.count(3))

#13 Convert array to string using tolist() method
print("Step 13")
a10 = array('i',[10,29,32,12])
my_list = a10.tolist()  
print(my_list)

#14 Append a string to char array using fromlist() method
print("Step 14")
list_1 = [12,3,4,56]
a11 = array('i',list_1)
print(a11)
print('\n')

#15 Slice element from array
print("Step 15")
a12 = array('i',[23,4,21,45,50])
print(a12[0:3])
print(a12[4:0:-1])