def reverseList(ls, start, end):
    ls[start:end+1] = reversed(ls[start:end+1])

mylist = [1,2,3,4,5,6,7]
reverseList(mylist, 0, 3)
reverseList(mylist, 4, 6)
reverseList(mylist,0,6)
print(mylist)


