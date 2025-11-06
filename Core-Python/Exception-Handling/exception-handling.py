a = int(input("Enter a Number:"))
b = int(input("Enter a Number:"))
try :
    res = a/b
    print(res)
# except ZeroDivisionError:
#     print("Not Divisible")
except Exception as e:
    print("error occurred")