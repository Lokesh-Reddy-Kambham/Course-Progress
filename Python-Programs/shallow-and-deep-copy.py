"""Shallow Copy"""
l = [10,20,30,40]
print(l)
l1 = l # shallow copy
print(l)
print(l1)
del l1[1]
print(l)
print(l1)

"""deep copy"""
a = [10,20,30,40,50]
print(a)
a1 = a.copy()
print(a)
print(a1)
del a[3]
print(a)
print(a1)
