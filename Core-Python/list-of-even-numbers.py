def even(num1):
    if num1%2==0:
        return True
    else:
        return False
l = []
i = 0
while i<=4:
    print("Enter a num:")
    num = int(input())
    l.insert(i,num)
    i = i+1
print(l)

i = 0
while i <=4:
    data = l[i]
    choice = even(l[i])
    if choice:
        print(l[i])
    i = i+1

