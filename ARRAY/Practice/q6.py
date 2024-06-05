# Find if two list are permuation of each other

ls1 = [29,23,24,26]
ls2 = [26,23,29,24]

def is_permutation(ls1, ls2):
    if len(ls1) != len(ls2):
        return False
    ls1.sort()
    ls2.sort()
    if ls1 == ls2:
        return True
    else:
        return False

print(is_permutation(ls1,ls2))

ls1 = ['a', 'b', 'c', 'd', 'e', 'f']
ls2 = ['b', 'd', 'e', 'f', 'a', 'c']
print(is_permutation(ls1,ls2))
    