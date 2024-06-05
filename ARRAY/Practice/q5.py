# Find if a list have all unique values

myList = [19,20,30,44,15,56,57,18,19,10,31,12,13,14,35,16,27,58,21]
def is_unique(myList):
    for i in range(len(myList)):
        for j in range(i+1,len(myList)):
            if myList[i] == myList[j]: 
                return False,i,j
    return True
print(is_unique(myList))

# Or
# def isUnique(myList):
#     a = []
#     for i in myList:
#         if i in a:
#             print(i)
#             return False
#         else:
#             a.append(i)
#     return True

# print(isUnique(myList))