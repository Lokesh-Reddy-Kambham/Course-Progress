def main():
    print("Inside main")
def outer(ptr):
    print("Inside outer")
    def inner():
        print("Inside inner")
        ptr1 = ptr
        ptr1()
        print("Leaving Inner")
    return inner()
outer(main)

def main():
    print("Inside main")
def outer(ptr):
    print("Inside outer")
    def inner():
        print("Inside inner")
        ptr1 = ptr
        ptr1()
        print("Leaving Inner")
    return inner
ref = outer(main)
ref()


















