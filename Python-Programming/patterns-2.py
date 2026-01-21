"""
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
"""
a = int(input("Enter Number:"))
for i in range(1,a+1):
    for space in range(1,a-i+1):
        print(" ",end=" ")
    x = 1
    for j in range(1,i+1):
        print(x,end=" ")
        x = x +1
    x = i -1
    for k in range(1,i):
        print(x,end=" ")
        x = x -1
    print()
"""
        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5
"""
b = int(input("Enter Number:"))
for i in range(1,b+1):
    for space in range(1,b-i+1):
        print(" ",end=" ")
    x = i
    for j in range(1,i+1):
        print(x,end=" ")
        x = x -1
    x = 2
    for k in range(1,i):
        print(x, end=" ")
        x = x+1
    print()
"""
      1
    2 3 4
  5 6 7 8 9
"""
c = int(input("Enter Number:"))
x = 1
for i in range(1,c+1):
    for space in range(1,c-i+1):
        print(" ",end=" ")
    for j in range(1,2*i):
        print(x,end=" ")
        x = x+1
    print()
"""
4 3 2 1
8 7 6 5
12 11 10 9
16 15 14 13
"""
d = int(input("Enter Number:"))
for i in range(1,d+1):
    temp = d*i
    for j in range(1,d+1):
        print(temp,end=" ")
        temp = temp -1
    print()
"""
A B C D E 
  A B C D 
    A B C 
      A B 
        A 
"""
e = int(input("Enter Number:"))
for i in range(1,e+1):
    order = 65 # order = ord("A")
    for j in range(1,e+1):
        if i <= j:
            print(chr(order),end=" ")
            order = order + 1
        else:
            print(" ",end=" ")
    print()
"""
L M N O P 
  M N O P 
    N O P 
      O P 
        P 
"""
f = int(input("Enter Number:"))
for i in range(1,f+1):
    order = ord("L")+i-1 # order = (65+11)+ i-1
    for j in range(1,f+1):
        if i <= j:
            print(chr(order),end=" ")
            order = order + 1
        else:
            print(" ",end=" ")
    print()