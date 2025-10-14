a = []
i = 0
while True:
    print("Enter a value:")
    data = int(input())
    a.insert(i,data)
    i = i+1
    print("Do you Want to Continue?: ")
    print("press 1:YES")
    print("press 2:No")
    choice = int(input())
    if choice == 1:
        pass
    else:
        break
print(a)

