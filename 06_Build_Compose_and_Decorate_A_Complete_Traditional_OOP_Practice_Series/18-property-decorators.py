class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Private attribute

    @property
    def price(self):
        return self._price  # Getter for price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value  # Setter for price

    @price.deleter
    def price(self):
        print("Deleting the price")
        del self._price  # Deleter for price

# Example usage
product = Product("Laptop", 1000)

# Getting the price using @property
print("Price:", product.price)

# Setting the price using @price.setter
product.price = 1200
print("Updated Price:", product.price)

# Trying to set a negative price
product.price = -500  # Should print a warning

# Deleting the price using @price.deleter
del product.price
