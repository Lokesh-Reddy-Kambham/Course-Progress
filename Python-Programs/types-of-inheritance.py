"""Single-Level inheritance"""
class A:
    def display_a(self):
        print("Parent class A")
class B(A):
    def display_b(self):
        print("Child Class B")
"""Multi-Level inheritance"""
class X:
    def display_x(self):
        print("Parent class X")
class Y(X):
    def display_y(self):
        print("Child Class Y which is derived from Class X")
        print("Parent for Class Z")
class Z(Y):
    def display_z(self):
        print("Child Class Z which is derived from Class Y")
"""Hierarchical Inheritance"""
class I:
    def display_i(self):
        print("Parent class I")
class J(I):
    def display_j(self):
        print("Derived from Class I")
class K(I):
    def display_k(self):
        print("Derived from class I")