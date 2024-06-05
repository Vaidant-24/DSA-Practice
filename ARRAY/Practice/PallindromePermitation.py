# if two or more character in string are odd in numbers then string is not pallindrome 
from collections import Counter

s = "cababcab"

def isPallindromePermutation(s):
    count = Counter(s)
    print(count)
    cnt = 0
    for num in count.values():
        if num % 2 != 0:
            cnt += 1
    return cnt < 2

print(isPallindromePermutation(s))

