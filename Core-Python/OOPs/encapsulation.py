class Book:
    def __init__(self,title,page):
        self._heading = title
        self.__pages = page

b1 = Book("Travelling",69)
print(b1._heading)
#print(book1.__pages)



