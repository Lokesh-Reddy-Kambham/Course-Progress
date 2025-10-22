class Animal:
    def eat(self):
        print("i am hungry to eat!")
    def sleep(self):
        print("it's sleeping time!")
    def breath(self):
        print("breath to live")
class Lion(Animal):
    pass
    # def hunt(self):
    #     print("It's time to hunt")
class Tiger(Animal):
    pass
    # def drink(self):
    #     print("Iam Thirsty, time to Drink")
class GodZilla(Animal):
    pass
    # def Destroy(self):
    #     print("Killing it up Brutal!")
    # def slogan(self):
    #     print("Thiraganana Dhoota")
l1 = Lion()
t1 = Tiger()
g1 = GodZilla()
l1.eat()
t1.sleep()
g1.breath()

