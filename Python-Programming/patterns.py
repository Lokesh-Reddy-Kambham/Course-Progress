"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
m = int(input("Enter Number:"))
for i in range(1,m+1):
    for j in range(1,m+1):
        print(i,end=" ")
    print()
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
n = int(input("Enter Number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
"""
method - 1
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""
o = int(input("Enter Number:"))
for i in range(1,(o*o)+1):
    if i %o == 0:
        print(i)
    else:
        print(i,end=" ")
"""
method - 2
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
"""
t = int(input("Enter Number:"))
x = 1
for i in range(1,t+1):
    for j in range(1,t+1):
        print(x,end=" ")
        x = x+1
    print()
"""
1 0 1 0
1 0 1 0
1 0 1 0
1 0 1 0
"""
p = int(input("Enter Number:"))
for i in range(1,p+1):
    for j in range(1,p+1):
        print(j%2,end=" ")
    print()
"""
method -1
1 2 3 4 0
1 2 3 4 0
1 2 3 4 0
1 2 3 4 0
1 2 3 4 0
"""
r = int(input("Enter Number:"))
for i in range(1,r+1):
    for j in range(1,r+1):
        if j == r:
            print(0,end=" ")
        else:
            print(j,end=" ")
    print()
"""
method - 2
1 2 3 4 0
1 2 3 4 0
1 2 3 4 0
1 2 3 4 0
1 2 3 4 0
"""
s = int(input("Enter Number:"))
for i in range(1,s+1):
    for j in range(1,s+1):
        print(j%r,end=" ")
    print()
"""
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 1 0
"""
u = int(input("Enter Number:"))
for i in range(1,u+1):
    for j in range(1,u+1):
        if j%2==0:
            print(1,end=" ")
        else:
            print(0,end=" ")
    print()
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
v = int(input("Enter Number:"))
value = 1
for i in range(1,v+1):
    for j in range(1,i+1):
        print(value, end=" ")
        value +=1
    print()
"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
x = int(input("Enter Number:"))
for i in range(1,x+1):
    temp = x
    for j in range(1,i+1):
        print(temp,end=" ")
        temp -=1
    print()
"""
5 6 7 8 9 
4 5 6 7 
3 4 5 
2 3 
1 
"""
y = int(input("Enter Number:"))
for i in range(1,y+1):
    value2 = y-i+1
    for j in range(1,y-i+2):
        print(value2,end=" ")
        value2 += 1
    print()
z = int(input("Enter Number:"))
for i in range(1,z+1):
    for space in range(1,z-i+1):
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