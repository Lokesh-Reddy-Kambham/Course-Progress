from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Making sounds")
d1 = Dog()
d1.make_sound()
