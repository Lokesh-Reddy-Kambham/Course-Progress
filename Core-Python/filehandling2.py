#read()
ptr = open("uppi.txt","r")
res = ptr.read()
print(res)
ptr.close()

#read(bytes)
ptr = open("uppi.txt","r")
res = ptr.read(9)
print(res)
ptr.close()

#readline
ptr = open("uppi.txt","r")
res = ptr.readline()
print(res)
ptr.close()

#readlines()
ptr = open("uppi.txt","r")
res = ptr.readlines()
print(res)
ptr.close()

#tell()
ptr1 = open("uppi.txt","r")
pos1 = ptr1.tell()
print(pos1)

pos2 = ptr1.read(4)
print(pos2)

pos3 = ptr1.tell()
print(pos3)

#seek()
pos4 = ptr1.seek(6)
print(pos4)

pos5 = ptr1.tell()
print(pos5)

ptr1.close()

