def fun1():
    print("Entering fun1")
    try:
        fun2()
    except Exception:
        print("Error occurred in fun1")
    print("Leaving Fun1")
def fun2():
    print("Entering Fun2")
    res = 10/0
    print(res)
    print("Leaving Fun2")
print("program started")
fun1()
print("Program ended")