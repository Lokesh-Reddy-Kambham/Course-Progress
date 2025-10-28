class A:
    def display(self):
        print("Inside A")
class B(A):
    def display(self):
        print("Inside B")
class C(B):
    def display(self):
        print("Inside C")

c1  = C()
c1.display()
c1.display()
c1.display()
