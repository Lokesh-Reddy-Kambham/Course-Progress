a = 10
def func1():
    global a
    a = 100
    b = 200
    print(a)
    print(b)
def func2():
    global a
    a = 150
    b = 250
    print(a)
    print(b)
print(a)
func1()
print(a)
func2()
print(a)
