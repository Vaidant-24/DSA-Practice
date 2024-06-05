st = 'geeks'

def revString(st):
    st1 = ''
    for i in st:
        st1 = i + st1
    return st1

def revStr(st):
    return st[::-1]

print(revString(st))
print(revStr(st))