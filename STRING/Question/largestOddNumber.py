s = "24546"
def largestOddNumber(s):
    num = int(s)
      
    while num % 2 == 0 and num != 0:
        num = num // 10
    if num % 2 != 0:
        return num
    else:
        return ""

print(largestOddNumber(s))