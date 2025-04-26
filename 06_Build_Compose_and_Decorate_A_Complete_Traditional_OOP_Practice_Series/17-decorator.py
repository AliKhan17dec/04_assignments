# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

# Applying the class decorator
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Example usage
p = Person("Ali")
print(p.greet())  # Method added via decorator
