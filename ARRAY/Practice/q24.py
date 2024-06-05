# Find union of arrays:-

num1 = [1,1,2,3,4,5]
num2 = [2,2,3,4,6]

# Using Optimal Approach:-
def Union(num1,num2):
    n1 = len(num1)
    n2 = len(num2)
    union = []
    i = j = 0
    while i < n1 and j < n2:
        if num1[i] <= num2[j]:
            if union == [] or union[-1] != num1[i]:
                union.append(num1[i])
            i += 1
        elif num1[i] > num2[j]:
            if union == [] or union[-1] != num2[j]:
                union.append(num2[j])
            j += 1
        
    while i < n1:
        if union == [] or union[-1] != num1[i]:
            union.append(num1[i])
        i += 1

    while j < n2:
        if union == [] or union[-1] != num2[j]:
            union.append(num2[j])
        j += 1

    return union

print(Union(num1, num2))

