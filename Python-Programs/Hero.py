class Hero:
    def __init__(self):
        self.name = "Uppendra"
        self.favMovie = "UI"
        self.noOfMovies = 60
    def skillSet(self):
        print("Uppendra is Actor and Director")

h1 = Hero()
print(h1.name)
print(h1.favMovie)
print(h1.noOfMovies)
h1.skillSet()
