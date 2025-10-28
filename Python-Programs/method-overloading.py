class A:
    def display(self,a):
        print(a)
class B(A):
    def display(self,a,b):
        print(a)
        print(b)
class C(B):
    def display(self,a,b,c):
        print(a)
        print(b)
        print(c)

c1 = C()
c1.display(10,20,30)
"""Method Overloading Is not supports in Python"""
c1.display(10,20)
c1.display(10)

