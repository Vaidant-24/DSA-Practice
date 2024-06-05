def longestCommonPrefix(strs) -> str:
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        l = strs[0]
        for word in strs:
            l = word if len(word) < len(l) else l
        for i in range(len(l)):
            for word in strs:
                if word[i] != l[i]:
                    return l[:i]
        return l
    
strs = ["flower" , "flow", "fling"]
print(longestCommonPrefix(strs))