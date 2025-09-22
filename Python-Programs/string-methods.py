str1 = input("Enter a String:")
print(str1)
if str1.isalpha():
    print("string contains only Alphabets")
elif str1.isdigit():
    print("string contains only Digits")
elif str1.isalnum():
    print("string contains Both")
else:
    print("string contains Some Other Characters")