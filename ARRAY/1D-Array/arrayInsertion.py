from array import array as arr
from array import *

a1 = arr('i',[23,34,56,32,43])

a2 = arr(a1.typecode,[24,53,67])
print(a2)
print(a2.buffer_info())
a2.insert(0,1)   # O(n)
print(a2)
a2.insert(2,1)   # O(n)
print(a2)
a2.insert(5,1)   # O(1)
print(a2)