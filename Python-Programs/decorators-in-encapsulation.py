class Person:
    def __init__(self):
        self.__name = ""

    @property
    def dataAcess(self):
        return self.__name
    @dataAcess
    def dataAcess(self,val):
        self.__name = val

p1 = Person()
p1.dataAcess = "Lokesh"
res = p1.dataAcess
print(res)
