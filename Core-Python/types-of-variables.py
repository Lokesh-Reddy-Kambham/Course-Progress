class Car:
    def __init__(self):
        self.brand="jaguar"
        self.cost=50000
    def drift(self):
        print("Car is Drifting")
        self.color="black"
c1 = Car()
print(c1.brand)
print(c1.cost)
print(c1.drift())
print(c1.color)
c1.color="purple"
print(c1.color)
c1.mileage=18
print(c1.mileage)