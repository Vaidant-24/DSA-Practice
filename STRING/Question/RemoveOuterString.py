def removeOuterparenthesis(s):
    res = ""
    cnt = 0
    
    for i in s:
        if i == '(':
            if cnt > 0:
                res = res + i
            cnt += 1
        else:
            cnt -= 1
            if cnt > 0:
                res = res + i
    return res

s = "(()())(())(()(()))"
print(removeOuterparenthesis(s))