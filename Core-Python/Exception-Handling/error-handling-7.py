try:
    a = int(input("Enter a Number:"))
    b = int(input("Enter a Number:"))
    res = a/b
    print(res)
except Exception as e:
    print(e.__str__())
    print(e)