#Problem 1: Check Whether the number is Even or Odd
n = int(input("Enter a Number:"))
if n%2 == 0 :
    print("Given Number is Even")
else:
    print("Given Number is Odd")

#Problem 2: Check Whether the string has Exactly 5 characters or not
s1 = input("Enter a String")
if len(s1)==5:
    print("Given String has 5 Characters")

#Problem 3: Check Whether the Given interger is 2 digit number or not
value = int(input("Enter the Num:"))
if 10<=n<=99:
    print("Given Number is 2 Digit Number")
else:
    print("Given Number is not 2 Digit Number")

#Problem 4: Check Whether the Given Integer is Multiple of 5 and Divisible by 3
n1 = int(input("Enter a Number:"))
if n1%5==0 and n%3==0:
    print("Given Integer is Multiple of 5 and Divisible by 3")
else:
    print("Given Integer is not Multiple of 5 and Divisible by 3")

#Problem 5: Check Whether the given String is Upper Case or not
s2 = input("Enter a String:")
if s2 == s2.upper():
    print("Given string is in uppercase")
else:
    print("Given string is not in uppercase")

def fun(data):
    return type(data) == float
print(fun(5.0))