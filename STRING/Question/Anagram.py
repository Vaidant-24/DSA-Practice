s1 = "silent"
s2 = "listen"

def checkAnagram(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    
    if l1 == l2:
        for i in s1:
            if i not in s2:
                return False
    else:
        return False
    return True

print(checkAnagram(s1,s2))
print(checkAnagram("abba","abab"))           
print(checkAnagram("abbac","cabab")) 
print(checkAnagram("abba","aaac"))    
print(checkAnagram("abba","ababab"))                            
print()

def Anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    s1 = sorted(s1)
    s2 = sorted(s2)
    
    return s1 == s2

print(Anagram(s1,s2))
print(Anagram("abba","abab"))           
print(Anagram("abbac","cabab")) 
print(Anagram("abba","aaac"))    
print(Anagram("abba","ababab"))


def EfficientAnagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    count = [0] * 256       # For storing index for ascii characters
    
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
        
    for x in count:
        if x != 0:
            return False
    
    return True

print()
print(EfficientAnagram(s1,s2))
print(EfficientAnagram("abba","abab"))           
print(EfficientAnagram("abbac","cabab")) 
print(EfficientAnagram("abba","aaac"))    
print(EfficientAnagram("abba","ababab"))

