class Mobile:
    def __init__(self):
        self.brand="Redmi"
    def call(self):
        print("Incoming call from Lover!!!")
    @staticmethod
    def game():
        print("Uppi is Gamer")
    @classmethod
    def sleep(cls):
        print("Uppi is sleeping")
        
m1= Mobile()
m1.call()
# m1.game()      """Not a standard way and not Recommended"""
# m1.sleep()
Mobile.game()
Mobile.sleep()
class Redmi(Mobile):
    def __init__(self):
        super().__init__()
    