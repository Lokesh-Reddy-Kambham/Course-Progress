try:
    a = int(input("Enter a Number:"))
    b = int(input("Enter a Number:"))
    res = a/b
    print(res)
except (ZeroDivisionError,ValueError )as e:
    print("it is Zero Division Error or Value Error")
except Exception as e:
    print("Some Other Error")
