a = 10
def outer():
    a = 15
    def inner():
        a = 20
        print(a)
    inner()
outer()

from math import pi
# pi = 10
def outer():
    # pi = 15
    def inner():
        # pi = 200
        print(pi)
    inner()
outer()
