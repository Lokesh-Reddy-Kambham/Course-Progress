class Brain:
    def __init__(self):
        self.status = "Active"
    def getBrain(self):
        print("Brain is Thinking")
class Person:
    def __init__(self,name):
        self.pname = name
        self.b = Brain()
        self.c = ""
    def hasCar(self,p):
        self.c = p
class Car:
    def __init__(self,name):
        self.cname = name
    def getCar(self):
        print("A Person Driving the Car")
b1 = Brain()
p1 = Person("Uppi")
c1 = Car("Jaguar")
p1.hasCar(c1)
print(p1.c.cname)
print(p1.b.getBrain())
del Person
print(c1.cname)
