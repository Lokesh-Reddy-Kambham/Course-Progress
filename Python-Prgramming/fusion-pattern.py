n = int(input("Enter Number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end="")
    print()

n = 4
for i in range(1,n+1):
    for space in range(1,i):
        print(" ",end=" ")
    for j in range(1,n-i+2):
        print("*",end=" ")
    for k in range(1,n-i+1):
        print("*" ,end=" ")
    print()
n=3
for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    for k in range(1,i+2):
        print("*" ,end=" ")
    print()
