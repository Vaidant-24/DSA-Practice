# is Substring or not 

s1 = "geeks"
s2 = "geeksforgeeks"

print(s1 in s2)

# Concatenation

s1 = "Welcome "
s2 = "GFG"

s3 = s1+"to the course of "+s2
print(s3)

# Get Index:

s1 = "geeks"
s2 = "geeksforgeeks"

print(s2.index(s1))
print(s2.rindex(s1))

# Find():

print(s2.find(s1))
print(s2.find(s1,1,len(s1)))