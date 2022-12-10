"""
a = 100
print(a)
print(id(a))

print("--------------------------")

b = 100
print(b)
print(id(b))

print("*********************")
name1 = "Anil"
print(name1)
print(id(name1))

name2 = "Anil"
print(name2)
print(id(name2))

# name1[2] = "y"
"""

a = [10, 20, 30, 40]
b = [10, 20, 30, 40]

print(id(a))
print(id(b))

c = [10, 20, 30, 40]
c[1] = 200
c[2] = 300
print(c)

