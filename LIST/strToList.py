
# Convert string to list Using list() and split
mystr1 = "Hello-World!"
ls1 = list(mystr1)
delimiter = '-'
ls2 = mystr1.split(delimiter)
print(ls1)
print(ls2)

delimiter = '-'
mystr2 = "12-34-56-78-9"
lst = mystr2.split(delimiter)
print(lst)


# Convert list to string using join()
delimiter = '_'

newList = [1,1,0,1,1,1]
myls = str(newList)
# newStr = delimiter.join(ls1)
# print(newStr)
print(type(myls))
