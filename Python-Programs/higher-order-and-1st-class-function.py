def fun1():
    print("Inside the fun1")
def fun2(ref):
    print("Entering the fun2")
    ref()
fun1()
fun2(fun1)
