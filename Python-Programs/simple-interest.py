class Farmer:
    def __init__(self,p,t,r):
        self.price = p
        self.time = t
        self.rate = r
    def loan(self):
        simple_interest = (self.price*self.time*self.rate)/100
        return simple_interest
f1 = Farmer(200000,3,2.5)
print(f1.loan())
