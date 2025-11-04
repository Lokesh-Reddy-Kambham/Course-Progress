import pickle
class Employee:
    def __init__(self,name,age):
        self.ename = name
        self.eage = age
    def disp(self):
        print(self.ename)
        print(self.eage)
e1 = Employee("Loki",22)
f = open("uppi.txt","wb")
pickle.dump(e1,f)
f.close()

