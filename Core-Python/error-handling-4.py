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
        val = int(input())
        val2 = int(input())
        res = val/val2
        print(res)
    except Exception as e:
        print("Error Occured in Fun 2")
        raise  e
    finally:
        print("Leaving fun2")
print("program started")
fun1()
print("Program ended")