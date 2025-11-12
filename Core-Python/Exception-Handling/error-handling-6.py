try:
    a = int(input("Enter a Number:"))
    b = int(input("Enter a Number:"))
    res = a/b
    print(res)
except ZeroDivisionError as e:
    print("it is Zero Division Error")
except ValueError as e:
    print("It is Value Error")
except Exception as e:
    print("Some Other Error")