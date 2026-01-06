# vowel or consonant checker
ch = input("Enter a Aplhabet:")
if "a" <= ch <= "z" or "A" <=ch <="Z":
    if ch.lower() in  "aeiou":
        print("vowel")
    else:
        print("consonant")
else:
    print("it's not Alphabet")

# username and password credientials
user_name = "Lokesh"
password = "Lokesh6969"
usr = input("Enter Username:")
pwd = input("Enter Password:")
if user_name == usr:
    if password == pwd:
        print("Successfully login")
    else:
        print("Invalid password")
else:
    print("Invalid username")

# Reverse a string whether the string starts with uppercase and ends with digit
""" code 1 """
value = input("Enter a String:")
if value[0].isupper():
    if value[-1].isdigit():
        print(f"reversed string {value[::-1]}")
    else:
        print("Not Ending with digit")
else:
    print("not starting with uppercase")

""" code 2 """
if "A" <=value <= "Z":
    if "0" <= value <=9 :
        print(f"reversed string {value[::-1]}")
    else:
        print("Not Ending with digit")
else:
    print("not starting with uppercase")
# display 1 to 5 number
i = 1
while i<=5 :
    print(i)
    i +=1  # i = i+1
# display even from 1 to 10
j = 0
while j<=10 :
    print(j)
    j +=2 # j = j+1
# display numbers from 1 to N which are multiple of 5
k = 1
value2 = int(input("Enter Number:"))
while k<=value2 :
    if k %5==0:
        print(k)
        k = k+1 # k+=1
# display numbers from 5 to 1
n = int(input("Enter a Number:"))
i = n
while i >=1 :
    print(i)
    i -=1 # i = i -1
# display divisors of a number
n1 = int(input("Enter Number:"))
for i in range(1,n1+1):
    if n1%i==0 :
        print(i ,end=" ")
# display divisors of every number from 1  to N
n2 = int(input("Enter Number:"))
for i in range(1,n2+1):
    print(i," : ",end=" ")
    for j in range(1,i+1):
        if i%j ==0 :
            print(j,end=" ")
    print()