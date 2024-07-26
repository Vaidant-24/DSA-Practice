# Note: 
  # a = 97
  # A = 65
  # a | ' ' = A
  # A & ~(' ') = A
  # a ^ (' ') = A
  # A ^ (' ') = a

def upperToLower(s:str) -> str:
    r = ""
    for c in s:
        r += chr((ord(c) | 32))
    return r

def lowerToUpper(s:str) -> str:
    r = ""
    for c in s:
        r += chr((ord(c) & ~ord(' ')))
    return r

def toggleCase(s:str) -> str:
    r = ""
    for c in s:
        r += chr((ord(c) ^ 32))
    return r


s = "zxyWTVUvW"
print(s)
print(upperToLower(s))
print(lowerToUpper(s))
print(toggleCase(s))