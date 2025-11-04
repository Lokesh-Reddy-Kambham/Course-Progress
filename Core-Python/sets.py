#1
s = {10,20,30,40}
print(s)
s1 = {10,"rama",3.14}
print(type(s1))
print(s1)
s2 = {10,20,30,20,40,10}
print(s2)
s3 = {}
print(type(s3))
s4 = set()
print(type(s4))

#2
s4 = set()
s4.add(10)
print(s4)
# s4.add(10,20,30)
print(s4)
s4.update([20,30,40])
s5 = {10,20,30,40,50}
s5.remove(30)
print(s5)
s5.discard(20)
print(s5)
"""traversing in a set"""
s6 = {10,20,30}
for i in s6:
    print(s6)
"""enumerate()"""
s7 = {10,20,30,40}
for i ,v in enumerate(s7):
    print(i," ",v)
