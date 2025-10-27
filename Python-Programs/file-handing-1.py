# writing
data=input("enter a data")
ptr=open("uppi.txt","w")
ptr.write(data)
ptr.close()

#reading
ptr1 = open("uppi.txt", "r")
res = ptr1.read()
print(res)
ptr1.close()

#append
store = input("enter a name")
ptr2 = open("uppi.txt","a+")
output2 = ptr2.write(store)
ptr2.close()

ptr3 = open("uppi.txt","a")
for i in range(5):
    name =input()
    ptr3.write(name+'\n')
ptr3.close()
