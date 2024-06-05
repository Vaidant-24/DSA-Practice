# Startswith and Endswith:

s1 = "geeksforgeeks"

s2 = "geeks"

print(s1.startswith(s2))
print(s1.endswith(s2))

print(s1.startswith(s2,1))
print(s1.endswith(s2,1))


# Split():

st = "Geeks For Geeks"
s1 = st.split(" ")
print(s1)

st = "Geeks, For, Geeks"
s2 = st.split(", ")
print(s2)

st = "Geeks, For, Geeks"
s3 = st.split(" ")
print(s3)

st = "Geeks, For, Geeks"
s4 = st.split()
print(s4)

# Join():

st = "Jumanji, Welcome to the jungle!"
print(", ".join(st))

st1 = ["Jumanji", "Welcome", "to", "the", "jungle!"]
print(" ".join(st1))
print(",".join(st1))

# Strip():

st = "  Geeks  For  Geeks  "
print(st.strip())

st2 = "--Geeks--For--Geeks--"
print(st2.strip("-"))
print(st2.lstrip("-"))
print(st2.rstrip("- "))