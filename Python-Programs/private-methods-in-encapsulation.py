class Bottle:
    def __init__(self):
        self.brand = "Old Monk"
    def __store(self):
        print("Bottle stores Rummm")

    def helper(self):
        self.__store()
b1 = Bottle()
b1.helper()
