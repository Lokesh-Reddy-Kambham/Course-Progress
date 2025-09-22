str1 = "if you think you can or you can't, you are right"
print(str1)

print(str1.count("you"))

str2 = "you"
print(str2 in str1)

print(str1.index("you"))
print(str1.find("you"))

print(str1.rindex("you"))
print(str1.rfind("you"))

print(str1.find("python"))
try:
    print(str1.index("python"))
except :
    print("index error")
