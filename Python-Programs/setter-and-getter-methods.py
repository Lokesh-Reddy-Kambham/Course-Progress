"""Example 1"""
class Book:
    def __init__(self,title,page):
        self._heading = title
        self.__pages = page
    def setter(self,val): # Setting or Modifying value of Private variable
        if val>0:
            self.__pages = val
    def getter(self):      # Getting or Accessing Value from Private variable
        return self.__pages

b1 = Book("Travel",69)

print(b1._heading)
#print(book1.__pages)

res1 = b1.getter()
print(res1)

b1.setter(200)
res2 = b1.getter()
print(res2)

b1.setter(-88)
res3 = b1.getter()
print(res3)

"""Example 2"""
class Person:
    def __init__(self):
        self.__name =""
    def setter(self,val):
        self.__name = val
    def getter(self):
        return self.__name
p1 = Person()
p1.setter("lokesh")
output = p1.getter()
print(output)