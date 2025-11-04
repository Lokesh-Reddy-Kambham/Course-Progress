class Charger:
    def __init__(self,name):
        self.cname = name
    def getCharger(self):
        print("Charger is Available")
class Mobile:
    def __init__(self,name):
        self.mname = name
        self.c = ''
    def hasMobile(self,p):
        self.c = p
m1 = Mobile("ViVo")
c1 = Charger("C Type")
m1.hasMobile(c1)
m1.c.getCharger()
del m1
print(c1.cname)
