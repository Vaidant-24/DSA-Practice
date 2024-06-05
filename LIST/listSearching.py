ls = [10,20,30,40,50,'a', 'b', 'c', 'd', 'e', 'f']

#Using Linear search
def search(ls, element):
    for i in range(len(ls)):
        if ls[i] == element:
            return i
    return "No element found"

#Using IN operator
def search_in(ls, element):
    if element in ls:
        return ls.index(element)
    else:
        return "No element found"

print(search(ls,30))
print(search_in(ls,50))