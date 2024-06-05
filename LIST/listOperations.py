a = [1,2,3]
b = [4,5,6]

# +: Concatenate Operation
c = a + b
print(c)

# *: Repeatative Operation
d = a * 3   # Repeat 3-times
print(d)

# len(): Return length of list
print(len(a))

# max(): Return maximum value of list
print(max(a))

# min(): Return minimum value of list
print(min(a))

# sum(): Return sum of elements of list
print(sum(a))
ls = [10,20,30,40]

# avg(): Return average value of list
def avg(a):
    n = len(a)
    return sum(a)/n

print(avg(ls))

#practice:
print("Enter 'e' to exit:-")
mylist = []
while True:
    inp = input("Enter element:")
    if inp == 'e': break
    mylist.append(int(inp))
    average = sum(mylist)/len(mylist)   

print(mylist)
print('average:',average)
    
