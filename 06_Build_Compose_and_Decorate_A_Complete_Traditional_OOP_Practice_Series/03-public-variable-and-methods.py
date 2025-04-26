class Car:
    def __init__(self, brand):
        # Public variable
        self.brand = brand

    # Public method
    def start(self):
        print(f"The {self.brand} car has started.")

# Instantiate the class
my_car = Car("Toyota")

# Access public variable
print("Car Brand:", my_car.brand)

# Access public method
my_car.start()
