class A:
    def show(self):
        print("A's show method")

class B(A):
    def show(self):
        print("B's show method")

class C(A):
    def show(self):
        print("C's show method")

class D(B, C):  # D inherits from both B and C
    pass

# Create an object of D and call show
d = D()
d.show()

# Check the Method Resolution Order
print(D.__mro__)
