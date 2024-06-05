def rotateString(s: str, goal: str) -> bool:
        if len(s) == 0 or len(goal) == 0:
            return True
        
        newStr = s + s
        return True if newStr.find(goal)!= -1 else False
s = "abcde"
goal = "abced"
print(rotateString(s,goal))