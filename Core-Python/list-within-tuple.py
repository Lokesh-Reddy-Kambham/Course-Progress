t = ("sheela",[10,20,30])
print(id(t[1]))
name , marks = t
print(name)
print(marks)
t[1].append(40)
t[1].remove(20)
print(t)

print(id(t[1]))


