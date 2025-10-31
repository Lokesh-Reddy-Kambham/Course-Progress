class OS:
    def __init__(self,type):
        self.status = 'Active'
        self.type = type
        print("Os is Installing")
    def update(self):
        print("Os is Updating")

class Mobile:
    def __init__(self,name):
        self.mname = name
        self.o = OS()
    def getOS(self):
        print("setting OS")

m1 = Mobile("Redmi","mac")
print(m1.mname)
print(m1.o.status)
m1.o.update()
del m1

# print(m1.o.status)
