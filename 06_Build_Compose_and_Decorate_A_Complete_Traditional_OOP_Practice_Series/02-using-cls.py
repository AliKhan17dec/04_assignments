class Counter:
    # Class variable to keep track of object count
    count = 0

    def __init__(self):
        # Increment the counter whenever a new object is created
        Counter.count += 1

    @classmethod
    def display_count(cls):
        print("Total objects created:", cls.count)

# Example usage
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

Counter.display_count()  # Output: Total objects created: 3
