"""
*   *   *
  * * *
* * * * *
  * * *
*   *   *
"""
m=int(input("Enter Number:"))
for i in range(1,m+1):
    for j in range(1,m+1):
        if i == j or i == m//2+1 or j == m//2+1 or i+j== m + 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
* * * * * 
* *     * 
*   *   * 
*     * * 
* * * * * 
"""
n = int(input("Enter Number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i ==1 or j==1 or i==n or j == n  or i == j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()