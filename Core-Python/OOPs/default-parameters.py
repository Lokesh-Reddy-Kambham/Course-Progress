class Demo:
    def display(self,a=10,b=20,c=30):
        print(a,end=" ")
        print(b)
        print(c)
d1= Demo()
x = 11
y = 22
z = 33
d1.display()
d1.display(x)
d1.display(z)
d1.display(c=z)
d1.display(c=y,a=z,b=x)
