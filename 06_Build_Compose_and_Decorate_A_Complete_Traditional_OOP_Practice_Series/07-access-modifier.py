class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name            # Public variable
        self._salary = salary       # Protected variable
        self.__ssn = ssn            # Private variable

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN (inside class):", self.__ssn)

# Creating an object
emp = Employee("Ali", 50000, "123-45-6789")

# Accessing variables
print("Public (name):", emp.name)         # Works fine
print("Protected (_salary):", emp._salary)  # Works, but not recommended outside class

# Trying to access private variable
try:
    print("Private (__ssn):", emp.__ssn)
except AttributeError as e:
    print("Private (__ssn): Cannot access directly:", e)

# Accessing private variable using name mangling
print("Private (__ssn) via mangling:", emp._Employee__ssn)

# Using method to show all
emp.show_info()
