"""frozenset is also a set but which is immutable"""
s = frozenset([1,2,3])
print(s)
# s.add(4)
print(s)
# s.discard(2)
print(s)

"""nested set is not allowed in set"""
# s1 = {1,2,3,{4,5,6},7.8}
"""list within a set is not allowed"""
# s2 = {1,2,3,4,[5,6,7],8}
"""tuple within in a set is allowed"""
s3 = {1,2,3,4,5,(6,7,8,9),99}
