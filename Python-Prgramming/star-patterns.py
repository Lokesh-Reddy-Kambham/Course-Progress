# # *
# # * *
# # *   *
# # *     *
# # * * * * *
# m = int(input("Enter a Number:"))
# for i in range(1,m+1):
#     for j in range(1,m+1):
#         if i == j or j == 1 or i == m:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #         *
# #       * *
# #     *   *
# #   *     *
# # * * * * *
# n = int(input("Enter a Number:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if j == n or i+j == n+1 or i == n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# # * * * * *
# # *     *
# # *   *
# # * *
# # *
# o = int(input("Enter a Number:|"))
# for  i in range(1,o+1):
#     for j in range(1,o+1):
#         if i==1 or j==1 or i+j==o+1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# # * * * * *
# #   *     *
# #     *   *
# #       * *
# #         *
# p = int(input("Enter a Number:"))
# for  i in range(1,p+1):
#     for j in range(1,p+1):
#         if i==1 or j==p or i == j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
q = int(input("Enter Number:"))
for i in range(1,q+1):
    for j in range(1,q+1):
        if i == j or i+j == q+1:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()