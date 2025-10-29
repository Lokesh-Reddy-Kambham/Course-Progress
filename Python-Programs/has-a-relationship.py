class Radio:
    def __init__(self,m):
        self.m = m
        # self.n = n
    def turnOn(self,x):
        if x ==1:
            print("Radio is ON")
        else:
            print("Radio is OFF")
class Car:
    def __init__(self,cmin,cmax):
        self.cmin = cmin
        self.cmax = cmax
        self.r = Radio()
c1 = Car(30,69,r=7)
print(c1.cmin)
print(c1.cmax)
c1.r.turnOn(1)
# print(c1.r.__dict__)



