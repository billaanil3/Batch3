# 1. Lists can be created by using [] or list() function
# 2. List objects are Mutable 
# 3. List elements can be either mutable or immutable
# 4. Both negative and positive indexing supports
# 5. Insertion order is preserved
# 6. Duplicate elements are allowed
# 7. Heterogeneous elements are allowed

"""
list1 = []
print(type(list1))
print(id(list1))

list2 = list()
print(type(list2))
print(id(list2))

list3 = [10, 20, 30, "HCL", [100, 200]]
print(list3)
list3[1] = 120
list3[2] = 130
print(list3)

list4 = [10, 20, 30, "HCL", [100, 200]]
print(list4[2])  # postive indexing
print(list4[-3]) # Negative Indexing

list4.append(500)
list4.append(600)
print(list4)

list5 = [10, 20, 30, "HCL", [100, 200], 20, 30, 10, 30, 20]
print(list5)

"""
"""
a = [10,20,30,10,40,20,50,60]
# print(dir(a))
# 'append', 'clear', 'copy', 'count',
# 'extend', 'index', 'insert', 'pop',
# 'remove', 'reverse', 'sort'
a.append(100)
print(a)

print(a.count(60))
print(a.index(20))
print(a.index(20, 2))
a.insert(2, 300)
print(a)

a.pop(-2)
print(a)

a.remove(50)
print(a)

a.sort()
print(a)

a.reverse()
print(a)

# a.extend([400])

# print(a)

list1 = [100, 200, 300]
list2 = [400, 500, 600]
list1.extend(list2)
print(list1)

list2.clear()
print(list2)

list3 = list1.copy()
print(list3)
print(list1)
"""
"""
l = [[10,20],[40,50,60], [70,80,90]]
print(l[0][0])
print(l[1][1])
print(l[2][1])

print(l[-2][1])
print(l[-2][-2])
"""
"""
a = 10
b = str(a)
print(a, b, type(a), type(b))
"""

a = "Python"
b = list(a)
print(a)
print(b)

b[0] = "Z"
print(b)

result = "".join(b)
print(result)

