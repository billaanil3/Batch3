"""
name = " Python "
print(name)
print(type(name))
print(id(name))
# print(dir(name))


print(name.upper())
print(name.lower())

print(name.islower())
print(name.isupper())

print(len(name))
print(name.strip())

"""
"""
text = "Welcome to Python World"
words = text.split(" ")
print(words)
print(" ".join(words))
"""
# --------------- Slicing --------------------------
"""
name = "Python World New"
print(name[0:6]) #----->[0,1,2,3,4]
print(name[7:12]) # ---> 
print(name[10:])
print(name[:10])

print(name[-1])
print(name[-3:])  #--->[-3, -2]
print(name[-9:-4])
"""

name = """
    Python
    programming 
    Language
"""
print(name)