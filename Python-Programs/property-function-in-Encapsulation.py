class Person:
    def  __init__(self):
        self.__name = ""
    def getter(self):
        return self.__name
    def setter(self,val):
        self.__name = val
    get_set = property(getter,setter)
p1 = Person()
p1.get_set = "lokesh"
res = p1.getter()
print(res)