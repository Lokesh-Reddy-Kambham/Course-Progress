"""
  * * *
*       *
* * * * *
*       *
*       *
"""
a = int(input("Enter Number:"))
for i in range(1,a+1):
    for j in range(1,a+1):
        if (i==1 and 1<j<a) or (j==1 and i>1) or (i==3) or (j==a and i>1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
  * * *   
*       * 
*       * 
*       * 
  * * *   
"""
o = int(input("Enter Number:"))
for i in range(1,o+1):
    for j in range(1,o+1):
        if (i==1 and 1<j<o) or (j==1 and 1<i<o) or (i==o and 1<j<o ) or (j==o and 1<i<o):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
* 
* 
* 
* 
* * * * *
"""
l = int(input("Enter Number:"))
for i in range(1,l+1):
    for j in range(1,l+1):
        if j==1 or i ==l:
            print("*",end=" ")
    print()
"""
        *         
      *   *       
    *       *     
  *           *   
* * * * * * * * * 
"""
n = int(input("Enter Number:"))
for i in range(1,n+1):
    for j in range(1,n+n):
        if i==n or i+j == n+1 or j-i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()