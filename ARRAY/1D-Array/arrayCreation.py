from array import *
a1 = array('i',[-1,2,2,3,3,3,4,5,5,5,12]) #'i' - signed integer

a2 = array('f',[1.3,2.3,2.0])
for x in a2:
    print(x, end=' ')
print()

print(type(a1))
print(a1)
for x in a1:
    print(x,end=' ')
    
print()

i = 0
while i < len(a1):
    print(a1[i],end=' ')
    i += 1

print()

a1.append(6)
print(a1)
print(a1.count(5))
print(a1.index(5))
print(a1.pop())
# a1.remove(1)
print(a1)

print(a1.buffer_info())