a = int(input("Enter Number:"))
b = int(input("Enter Number:"))
c = int(input("Enter Number:"))

if a > b:
    if a>c:
        print("a Is Greater")
    elif a == c:
        print("a and c is Equal and Greater than b")
    else :
        print("c is Greater")
elif b>c:
    if a ==b:
        print("a and b are Equal and Greater than c")
    else:
        print("b is Greater")
elif c > a:
    if b == c:
        print("b and c are Equal and Greater than a")
    else:
        print("c is Greater")
else:
    print("All are Equal")

if a==b and b==c:
    print("All are Equal")
elif a>b and a>c:
    print("a is Greater")
elif b>c:
    if a==b:
        print("a and b are Equal and Greater than c")
    else:
        print("b is Greater")
else:
    if b == c:
        print("b and c are Equal and Greater than a")
    elif a ==c:
        print("a and c are Equal and Greater than b")
    else:
        print("c is Greater")