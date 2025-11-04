import copy
s = {"name":"munni","age":22,"phone":{"jio":420,"airtel":143},"address":"Russia"}
print(s)
#shallow copy
s1 = s
print(s)
print(s1)
s["age"] = 18
print(s)
print(s1)

# copy method
s2 = s.copy()
s["phone"]["jio"] = 424
print(s)
print(s2)

# deep copy
s3 = copy.deepcopy(s)
s["phone"]["airtel"] = 145
print(s)
print(s3)