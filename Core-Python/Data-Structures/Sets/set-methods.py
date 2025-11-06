s1 = {1,2,3,4}
print(s1)
s2 = {3,4,5,6}
print(s2)
s3 = s1.union(s2)
print(s3)
s4 = s1.intersection(s2)
print(s4)
s5 = s1.difference(s2)
print(s5)
s6 = s2.difference(s1)
print(s6)
s7 = s1.symmetric_difference(s2)
print(s7)

#disjoint() method
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3  = {5,6,7,8}
print(set1.isdisjoint(set2))
print(set2.isdisjoint(set3))
print(set1.isdisjoint(set3))

#subset() and superset() method
s11 = {1,2,3,4}
s22 = {1,2}
print(s11.issubset(s22))
print(s22.issubset(s11))
print(s11.issuperset(s22))
print(s22.issuperset(s11))

s33 = {1,2}
print(s22.issubset(s33))
print(s33.issuperset(s22))

