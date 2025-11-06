class Calci:
    def operations(self,a,b):
        r1 = a+b
        r2 = a-b
        r3 = a*b
        r4 = a/b
        return r1 , r2 , r3,r4
c1 = Calci()
x = 5
y = 2
res = c1.operations(x,y)
print(type(res))
print(res)

class Calculator:
    def operations1(self,a,b):
        r1 = a+b
        r2 = a-b
        r3 = a*b
        r4 = a/b
        return r1
c2 = Calculator()
x = 5
y = 2
res1 = c2.operations1(x,y)
print(type(res1))
print(res1)
