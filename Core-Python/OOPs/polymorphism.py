class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is Sleeping")
class Lion(Animal):
    def breath(self):
        print("Lion is Breathing")
class Tiger(Animal):
    def breath(self):
        print("Tiger is sleeping")
class Husky(Animal):
    def breath(self):
        print("Husky is sleeping")
l1 = Lion()
t1 = Tiger()
h1 = Husky()
# k1 = Animal()
def allowAnimal(ref):
    ref.eat()
    ref.sleep()
    ref.breath()
allowAnimal(l1)
allowAnimal(t1)
allowAnimal(h1)
# allowAnimal(k1)

