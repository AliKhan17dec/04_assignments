class Logger:
    def __init__(self):
        print("Logger started. Constructor called.")

    def __del__(self):
        print("Logger ended. Destructor called.")

# Example usage
logger = Logger()

# Optional: delete the object manually to trigger destructor immediately
del logger

# Or let it be destroyed automatically when the program ends
