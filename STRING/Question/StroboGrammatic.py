s = "191"
dic = {'1':'1', '0':'0', '8':'8', '6':'9', '9':'6'}
def check(s):
    n = len(s)
    if n % 2 == 0:
        n = n // 2
        s1 = s[0:n]
        s2 = s[n:]
    else:
        n = n // 2
        s1 = s[0:n]
        s2 = s[n+1:]
    s3 = s2[::-1]
    
    for i in range(len(s1)):
        if s1[i] != dic[s3[i]]:
            return False
    return True

def checkStroboGrammatic(s):
    i = 0 
    j = len(s) - 1
    while i <= j:
        if s[i] != dic[s[j]]:
            return False
        i += 1
        j -= 1
    return True
    

print(check(s))
print(checkStroboGrammatic(s))