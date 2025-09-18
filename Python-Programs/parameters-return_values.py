#no parameter no return value
class Calculator:
    def __init__(self):
        self.brand ="Casio"
        self.cost = 15777
    def add(self):
        a = 10
        b = 20
        c =a+b
        print(c)
c1 = Calculator()
c1.add()


#no parameter with return value
class Calculator:
    def __init__(self):
        self.brand ="Casio"
        self.cost = 15777
    def add(self):
        a = 10
        b = 20
        c =a+b
        return c
c2 = Calculator()
res = c2.add()
print(res)

#with parameter no return value
class Calculator:
    def __init__(self):
        self.brand ="Casio"
        self.cost = 15777
    def add(self,a,b):
        c = a+b
        print(c)
c3 = Calculator()
i = int(input())
j = int(input())
c3.add(i,j)

#with parameter and return value
class Calculator:
    def __init__(self):
        self.brand ="Casio"
        self.cost = 15777
    def add(self,a,b):
        return a + b
c4 = Calculator()
x = int(input())
y = int(input())
output = c4.add(x,y)
print(output)
