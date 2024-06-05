#Type - 1:Using %s

name = "ABC"
course = "GFG"

str = "Hi! %s Welcome to the %s course" % (name,course)
print(str)

#Type - 2: Using format()

str2 = "Hi! {} Welcome to the {} course".format(name,course)
print(str2)

#Type - 3:Using f string 

str3 = f"Hi! {name} Welcome to the {course} course"
print(str3)

a = 10
b = 100

str4 = f"The sum of a and b is {a + b} and the product is {a * b}"
print(str4)

s1 = "abc"
s2 = "XYZ"

s3 = f"{s1.upper()}"
print(s3)

s4 = f"{s2.lower()}"
print(s4)