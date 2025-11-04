class Student:
    def __init__(self,name,age,username):
        self.name = name
        self.age = age
        self.usn = username
        self.details = f"{self.name} {self.age} {self.usn}"
    def study(self):
        print(f"{self.name} is studying")

lokesh = Student("Lokesh",23,"l5711")
print(lokesh.name)
print(lokesh.age)
print(lokesh.usn)
print(lokesh.details)
lokesh.study()