print("abcd" < "zyxw")
print("abcd" < "z")
print("this" > "abcdefg" )
print("this" >= "abcdefg" )
print("abcd" > "abc")
print("abcd" >= "abc")
print("abc" <= "abc")

s1 = "gks"
s2 = "geeksforgeeks"
s3 = ''

for i,ch in enumerate(s2):
    if ch in s1:
        s3 += ch
print(s3)

s3 = "gksgksgksgks"
print(s3.find(s1))