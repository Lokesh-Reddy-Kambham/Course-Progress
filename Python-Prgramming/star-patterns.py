m = int(input("Enter a Number:"))
for i in range(1,m+1):
    for j in range(1,m+1):
        if i == j or j == 1 or i == m:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
n = int(input("Enter a Number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j == n or i+j == n+1 or i == n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()