class Student:
    def __init__(self,name:str,age:int,address:str):
        self.name = name
        self.age = age
        self.address = address
        self.full_details = f"{self.name} age:{self.age} from {self.address}"
vasco = Student("Vasco",23,"Tirupati")
print(vasco.full_details)
