# Custom exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function that checks age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be 18 or older.")
    else:
        print("Age is valid.")

# Example usage
try:
    check_age(16)  # This will raise the custom exception
except InvalidAgeError as e:
    print(f"Error: {e}")
