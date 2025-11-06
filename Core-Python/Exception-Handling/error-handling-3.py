def fun1():
    print("Entering fun1")
    try:
        fun2()
    except Exception:
        print("Error occurred in fun1")
    print("Leaving Fun1")
def fun2():
    print("Entering Fun2")
    try:
        res = 10/0
        print(res)
    except Exception as e:
        print("Error Occured in Fun 2")
        raise  e
    print("Leaving Fun2")
print("program started")
fun1()
print("Program ended")