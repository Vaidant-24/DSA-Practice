txt = "geeksforgeeks"
pattern = "geeks"

txt2 = "AAAA"
pattern2 = "AAA"

def patternIndex(txt,pattern):
    ans = []
    res = txt.find(pattern)
    while res != -1:
        print(res)
        res = txt.find(pattern,res + 1)
    

patternIndex(txt,pattern)
patternIndex(txt2,pattern2)