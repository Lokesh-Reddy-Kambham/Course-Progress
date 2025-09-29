def func1():
    print("Inside the fun1")

def func2():
    print("Inside the fun2")

print(func1)
print(func2)

ptr1 = func1
ptr2 = func2

ptr1()
ptr2()