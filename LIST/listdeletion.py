ls = ['a', 'b', 'c', 'd', 'e', 'f']

# List Slicing
print("List Slicing")
print(ls[0:3])
print(ls[:len(ls)])
print(ls[:len(ls):+2])
print(ls[:len(ls):+3])

# Pop Method: It delete the element of specified index
print("Pop Method")
ls.pop(0)
print(ls)
ls.pop()
print(ls)

# Remove Method: It delete the specified element 
ls.remove('c')
print(ls)

# Delete Method: It delete the elements of specified index-range
mylist = [2,4,5,6,7,8,9,10,11]

del mylist[0:5]
print(mylist)