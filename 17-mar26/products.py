# Operator Overloading
<<<<<<< HEAD
# Arithmetic: + (__add__), - (__sub__), = (__mul__), / (__truediv__)
# Comparison: == (__eq__), != (__ne__), < (__lt__), > (__gt__)

class Product:

=======
# Arithmetic: + (__add__), - (__sub__), * (__mul__), / (__truediv__)
# Comparison: == (__eq__), != (__ne__), < (__lt__), > (__gt__)

class Product:
    
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
    # constructor
    def __init__(self, name, price):
        self.name = name
        self.price = price
<<<<<<< HEAD

=======
    
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
    # Operator(s) overloading
    def __add__(self, other): # +
        #return self.price + other.price
        if isinstance(other, Product):
            return Product(f"{self.name}+{other.name}", self.price + other.price)
        return Product("Total", self.price + other)
<<<<<<< HEAD

=======
    
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
    def __radd__(self, other):
        if other == 0:
            return self
        return self.__add__()
    
    def __mul__(self, number):
        return Product(f"{number} {self.name}s", self.price * number)
<<<<<<< HEAD

    # CLI representation
=======
    
    # CLI represention 
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
    def __str__(self):
        """user friendly"""
        return f"{self.name}: ${self.price}"
    
    def __repr__(self):
        """developer friendly"""
<<<<<<< HEAD
        return self .__str__()

apple = Product("Apple", 2.55)
orange = Product("Orange", 1.88)
chips = Product("Lays", 4.99)

print(apple, orange)
print(apple + orange + chips)

cart = []
cart.append(apple)
cart.append(orange)
cart.append(chips)

print(cart)
print("Total in Cart: ", sum(cart))
=======
        return self.__str__()

apple = Product("apple", 2.55)
orange = Product("orange", 1.88)
chips = Product("lays", 4.99)

print(apple, orange)
print(apple + orange*26 + chips)

cart = []
cart.append(apple*3)
cart.append(orange*2)
cart.append(chips*5)

print(cart)
print("Total in Cart: ", sum(cart))




    
>>>>>>> 787920c879c2e5ba256e2dddafa4219b036c89e8
