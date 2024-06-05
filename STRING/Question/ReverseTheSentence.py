s = "the sky is blue"
s1 = "  the    sky   is   blue  "
def revSentence(s):
    newStr = ''
    temp = s.split(" ")
    
    for word in temp:
        newStr = word + " " + newStr
    return ''.join(newStr.strip(" "))

print(revSentence(s))
print(revSentence(s1))