class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Initialize with a multiplication factor

    def __call__(self, num):
        return num * self.factor  # Multiply the input by the factor

# Example usage
multiply_by_3 = Multiplier(3)

# Testing with callable() to check if the object is callable
print("Is multiply_by_3 callable?", callable(multiply_by_3))

# Using the object like a function
result = multiply_by_3(5)  # This will call __call__()
print("5 multiplied by 3 is:", result)
