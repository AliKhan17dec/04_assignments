class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking! Woof woof!")

# Example usage
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()
