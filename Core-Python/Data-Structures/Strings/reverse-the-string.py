# string = input("Enter a string")
# reverse =""
# for i  in string[::-1]:
#     reverse=reverse+i
# print(reverse)
#
# rev=""
# for i in string:
#     rev=i+rev
# print(reverse)
#
# print(string[::-1])
#
#

user = input("Enter a Sentence")
str1 = user.split()
str2 = str1[::-1]
print(" ".join(str2))
