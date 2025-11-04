string = "Uppi is Drinking"
print(string)

str1 = string.replace("is","was")
print(str1)

print(string.startswith("uppi"))
print(string.startswith("lokesh"))

print(str1.endswith("Dancing"))
print(str1.endswith("Drinking"))

print(id(string))
print(id(str1))
print(str1 is string)
