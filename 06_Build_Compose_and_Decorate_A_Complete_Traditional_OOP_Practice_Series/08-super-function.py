class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        # Call the constructor of the base class
        super().__init__(name)
        self.subject = subject

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Example usage
teacher = Teacher("Mr. Ali", "Physics")
teacher.display_info()
