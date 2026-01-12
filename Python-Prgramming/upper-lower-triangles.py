# # primary Diagonal
# n = int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(n+1):
#         if i == j:
#             print("*" ,end =" ")
#         else:
#             print(" ",end=" ")
#     print()
# # lower primary triangle
# m = int(input("Enter a Number:"))
# for i in range(1,m+1):
#     for j in range(m+1):
#         if i>j:
#             print("*" , end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# # upper primary triangle
# o = int(input("Enter a Number:"))
# for i in range(1,o+1):
#     for j in range(o+1):
#         if i<j:
#             print("*" , end=" ")
#         else:
#             print(" ", end=" ")
#     print()
# secondary diagonal
p = int(input("Enter a Number:"))
for i in range(1,p+1):
    for j in range(1,p+1):
        if i + j == p:
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()
# secondary lower triangle
q = int(input("Enter a Number:"))
for i in range(1,q+1):
    for j in range(1,q+1):
        if i + j < q:
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()
# secondary upper triangle
r = int(input("Enter a Number:"))
for i in range(1,r+1):
    for j in range(1,r+1):
        if i + j > r:
            print("*" ,end=" ")
        else:
            print(" ",end=" ")
    print()