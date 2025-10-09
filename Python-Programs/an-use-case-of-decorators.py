def main():
    return "lokesh"

def outer(ptr):
    print("Inside outer")
    def inner():
        print("inside Inner")
        pt1 = ptr()
        ans = pt1.lower()
        print(ans)
    return inner
ref = outer(main)
ref()