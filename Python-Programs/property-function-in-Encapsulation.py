class Person:
    def  __init__(self):
        self.__name = ""
    def getter(self):
        return self.__name
    def setter(self,val):
        self.__name = val
    get_set = property(getter,setter)#property method used in encapsulation
p1 = Person()
p1.get_set = "lokesh"
res = p1.getter()
print(res)