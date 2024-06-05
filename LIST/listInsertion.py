ls = [10,20,30,40,50,60,70]

# Update the list
for i in range(len(ls)):
    ls[i] = ls[i] * 100
    
print(ls)

# Insertion in the list

ls.insert(0,10)
print(ls)

ls.insert(3,33)
print(ls)

ls.insert(9,55)
print(ls)

ls.append(99)
print(ls)

ls.append(100)
print(ls)

ls2 = [2,4,6,8]
ls.extend(ls2)
print(ls)