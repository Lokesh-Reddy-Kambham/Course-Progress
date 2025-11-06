def outer():
    print("inside outer function")
    def inner():
        return "inside inner function"
    global res
    res = inner()
outer()
print(res)



def outer():
    print("inside outer function")
    def inner():
        print("inside inner function")
    return inner
res = outer()
res()

