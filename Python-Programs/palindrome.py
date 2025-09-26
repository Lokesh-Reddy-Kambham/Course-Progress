word = input("Enter a String:")
rev =''
for i in word:
    rev = i+rev
if word==rev:
    print("Is Palindrome")
else :
    print("Is not Palindrome")

if word ==word[::-1]:
    print("Is Palindrome")
else:
    print("Is not Palindrome")