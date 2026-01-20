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
version - 1
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
version - 2
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