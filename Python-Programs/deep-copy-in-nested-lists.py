"""Deep copy in Nested List"""
l = [10,20,30,["loki","lokesh"],40,50]
print(l)
l1 = l.copy() # d=Deep copy works like Shallow copy in nested list
print(l)
print(l1)
del l[3][1]
print(l)
print(l1)

"""To achieve Deep copy in nested lists we have to import deepcopy from copy"""
print("deep Copy works as deep copy")
import copy
a = [10,20,30,["loki","lokesh"],40,50]
print(a)
a1 = copy.deepcopy(a)
print(a)
print(a1)
del a[3][1]
print(a)
print(a1)
