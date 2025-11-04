class Farmer:
    r = 2.5
    def __init__(self,p:int,t:int):
        self.principle = p
        self.time = t
    def loan(self) -> None:
        si = (self.principle * self.time * Farmer.r)/100
        print(si)
f1 = Farmer(500000,7)
f2 = Farmer(7777777,8)
print(Farmer.r)
f1.loan()
f2.loan()
